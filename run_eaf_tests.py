import json
import argparse
import sys
from pathlib import Path

import runner


TESTS = {
    "Tst_066": [
        ("collapse.i", "files"),
        ("condense.i", "files"),
        ("convert.i", "files.convert"),
        ("printlib.i", "files"),
        ("test111.i", "files"),
        ("test112.i", "files"),
        ("test113.i", "files"),
        ("test114.i", "files"),
        ("allrun.i", "files"),
    ],
    "Tst_069":
    [
        ("collapse.i", "files"),
        ("condense.i", "files"),
        ("printlib.i", "files"),
        ("test21.i", "files"),
        ("test22.i", "files"),
        ("test23.i", "files"),
        ("test24.i", "files"),
        ("test27.i", "files"),
        ("allrun.i", "files"),
    ],
    "Tst_100":
    [
        ("collapse.i", "files"),
        ("condense.i", "files"),
        ("printlib.i", "files"),
        ("test1.i", "files"),
        ("test2.i", "files"),
        ("test3.i", "files"),
        ("test4.i", "files"),
        ("test5.i", "files"),
        ("test6.i", "files"),
        ("test6a.i", "files"),
        ("test7.i", "files"),
        ("test8.i", "files"),
        ("test9.i", "files"),
        ("test10.i", "files"),
    ],
    "Tst_175": [
        ("allrun.i", "files"),
        ("collapse.i", "files"),
        ("condense.i", "files"),
        ("printlib.i", "files"),
        ("test11.i", "files"),
        ("test12.i", "files"),
        ("test13.i", "files"),
        ("test14.i", "files"),
        ("test15.i", "files"),
        ("test16.i", "files"),
        ("test17.i", "files"),
        ("test18.i", "files"),
        ("test19.i", "files"),
        ("test20.i", "files"),
        ("test25.i", "files"),
        ("test26.i", "files"),
    ],
    "Tst_315": [
        ("allrun.i", "files"),
        ("collapse.i", "files"),
        ("condense.i", "files"),
        ("printlib.i", "files"),
        ("test70.i", "files"),
        ("test71.i", "files"),
        ("test72.i", "files"),
        ("test73.i", "files"),
        ("test74.i", "files"),
    ],
    "Tst_spec":
    [
        ("collapse.i", "files"),
        ("condense.i", "files"),
        ("allrun.i", "files"),
        ("printlib.i", "files"),
        ("test51.i", "files"),
        ("test52.i", "files"),
    ],
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output_file", required=False, default="results.json")
    args = parser.parse_args()
    output_file = args.output_file

    has_failure, all_results = runner.mp_run(TESTS, False)

    # write results to disk
    Path(output_file).write_text(json.dumps(all_results, indent=4, sort_keys=True))

    # check for errors
    if runner.check_all_errors(all_results) or has_failure:
        print("ERROR: Some tests failed")
        sys.exit(1)


if __name__ == "__main__":
    main()
