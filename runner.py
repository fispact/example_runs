"""A simple runner for FISPACT-II tests"""
import time
from typing import Optional, Union
import os
import shutil
import subprocess
import pathlib
from multiprocessing import Queue, Process

import pyfispact as pf

base_dir = pathlib.Path(__file__).parent.resolve()


class bc:
    GREEN = "\033[92m"
    RED = "\033[91m"
    UGREEN = "\033[92m\033[4m"
    URED = "\033[91m\033[4m"
    ENDC = "\033[0m"


_result_map = {
    True: f"{bc.GREEN}✔{bc.ENDC}",
    False: f"{bc.RED}✘{bc.ENDC}",
}



def get_log(log_name: Union[pathlib.Path, str]) -> pf.Monitor:
    m = pf.Monitor()
    pf.io.from_file(m, str(log_name))
    return m

def get_last_error(monitor: pf.Monitor) -> str:
    nrerrors = monitor.nrofmessages(pf.severity.error)
    nrfatals = monitor.nrofmessages(pf.severity.fatal)
    # get last errors
    if nrfatals > 0:
        error_message = monitor.get(nrfatals-1, pf.severity.fatal)
    elif nrerrors > 0:
        error_message = monitor.get(nrerrors-1, pf.severity.error)
    else:
        error_message = ""
    return error_message

def replace_in_file(file_name: Union[pathlib.Path, str], old: str, new: str) -> None:
    with open(file_name, "rt") as f:
        data = f.read()
    data = data.replace(old, new)
    with open(file_name, "wt") as f:
        f.write(data)

def enable_init_keyword(file_name: Union[pathlib.Path, str], keyword: str) -> None:
    ipath = pathlib.Path(file_name)
    input_content = ipath.read_text()
    lines = [x.strip() for x in input_content.split('\n')]
    fispact_keyword_index = lines.index('FISPACT')
    # add the init keywords before FISPACT keyword
    before_fispact = "\n".join(lines[:fispact_keyword_index])
    after_fispact = "\n".join(lines[fispact_keyword_index:])
    if keyword not in input_content:
        ipath.write_text(f"{before_fispact}\n{keyword}\n{after_fispact}")

def set_xs_type(file_name: Union[pathlib.Path, str], use_binary: bool):
    ipath = pathlib.Path(file_name)
    if use_binary:
        replace_in_file(ipath, "GETXS 1", "GETXS -1")
    else:
        replace_in_file(ipath, "GETXS -1", "GETXS 1")

def clean_up(name: str) -> None:
    # clean up before run
    pathlib.Path(base_dir / name / "COLLAPX").unlink(missing_ok=True)
    pathlib.Path(base_dir / name / "ARRAYX").unlink(missing_ok=True)
    for p in pathlib.Path(base_dir / name).glob("**/*"):
        if p.suffix in {".out", ".log", ".tab1", ".tab2", ".tab3", ".tab4", ".plt", ".gra", ".json"}:
            p.unlink()

def run_test_case(name: str, inputs: list[tuple[str, str]], use_binary: Optional[bool] = True) -> dict[str, dict]:
    """inputs should be input file name with .i and files file used"""
    fispact_exe = os.getenv("FISPACT")
    if fispact_exe is None:
        raise RuntimeError(
            "FISPACT env variable is not set, please point this to your binary for testing"
        )

    clean_up(name)
    output_dir = pathlib.Path('./outputs') / name
    output_dir.mkdir(parents=True, exist_ok=True)

    results = {"has_failure": False, "tests": {}}
    for input_file, files_file in inputs:
        ipath = base_dir / name / input_file
        fpath = base_dir / name / files_file

        result = {}
        if ipath.exists and fpath.exists:
            set_xs_type(ipath, use_binary=use_binary)
            enable_init_keyword(ipath, 'JSON')
            enable_init_keyword(ipath, 'CLOBBER')
            cmd = [fispact_exe, input_file, files_file]
            print(f"Running {name}::{input_file} ...")

            ts = time.time()
            proc = subprocess.run(
                cmd, capture_output=True, cwd=base_dir / name, universal_newlines=True
            )
            te = time.time()

            time.sleep(0.1)

            output_log = base_dir / name / input_file.replace(".i", ".log")
            output_json = base_dir / name / input_file.replace(".i", ".json")
            monitor = get_log(output_log)
            error_message = get_last_error(monitor)
            has_failure = proc.returncode != 0 or monitor.hasfatal()
            print(f"... result {name}::{input_file} {_result_map[not has_failure]}")

            # move the output json and log file
            if output_json.exists():
                shutil.move(output_json, output_dir / input_file.replace(".i", ".json"))
            shutil.move(output_log, output_dir / input_file.replace(".i", ".log"))

            result = {
                "json_file": f"./outputs/{name}/{input_file.replace('.i', '.json')}",
                "log_file": f"./outputs/{name}/{input_file.replace('.i', '.log')}",
                "has_failure": has_failure,
                "runtime": te-ts,
                "error_message": error_message
            }
            results["has_failure"] |= has_failure
        else:
            result = {
                "json_file": "",
                "log_file": "",
                "has_failure": True,
                "runtime": 0,
                "error_message": f"Test suite: {name}, with input: {input_file} does not exist. Please check your test cases."
            }
            results["has_failure"] = True
            print(f"Test suite: {name}, with input: {input_file} does not exist. Please check your test cases.")

        results["tests"][input_file.replace(".i", "")] = result

    clean_up(name)

    return results

def mp_run_test_case(queue: Queue, name: str, inputs: list[tuple[str, str]], use_binary: bool):
    """Multiprocess run using a queue"""
    try:
        r = run_test_case(name, inputs, use_binary=use_binary)
        queue.put({name: r})
    except Exception as e:
        queue.put({name: {"has_failure": True, "tests": {}}})
        print(e)


def mp_run(tests: dict[str, list[tuple[str, str]]], use_binary: Optional[bool] = True) -> tuple[bool, dict[str, dict]]:
    processes = []
    queue = Queue()
    has_failure = False
    for k, v in tests.items():
        p = Process(
            target=mp_run_test_case, args=(queue, k, v, use_binary,)
        )
        p.start()
        processes.append(p)

    all_results = {}
    # Wait for all processes to complete and check their exit codes
    for p in processes:
        p.join()
        try:
            result = queue.get(timeout=5)
            all_results = {**all_results, **result}
        except Exception as e:
            pass

        if p.exitcode != 0:
            has_failure = True

    return has_failure, all_results


def check_all_errors(all_results: dict) -> bool:
    errors = []
    for suite, results in all_results.items():
        if results["has_failure"]:
            return True

        for x in results["tests"].values():
           for k, v in x.items():
               if 'has_failure' == k:
                   errors.append(v)

    return any(errors)

