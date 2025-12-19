import json
import argparse
import sys
from pathlib import Path

import runner


TESTS = {
    "Tst_162prot": [
        ("collapse.i", "files"),
        ("condense.i", "files"),
        ("convert.i", "files"),
        ("printlib.i", "files"),
        ("test1.i", "files"),
        ("test2.i", "files"),
        ("test3.i", "files"),
        ("test4.i", "files"),
        ("test5.i", "files"),
    ],
    "Tst_162deut": [
        ("collapse.i", "files"),
        ("condense.i", "files"),
        ("convert.i", "files"),
        ("printlib.i", "files"),
        ("test31.i", "files"),
        ("test32.i", "files"),
        ("test33.i", "files"),
        ("test34.i", "files"),
        ("test35.i", "files"),
    ],
    "Tst_162gamm": [
        ("allrun.i", "files"),
        ("test71.i", "files"),
        ("test72.i", "files"),
    ],
    "Tst_162heli": [
        ("allrun.i", "files"),
        ("test71.i", "files"),
        ("test72.i", "files"),
    ],
    "Tst_709fns":
    [
        ("collapse.i", "files"),
        ("condense.i", "files"),
        ("Fe.i", "files"),
        ("FeAdjusted.i", "files"),
        ("Os.i", "files"),
        ("SS316.i", "files"),
        ("printlib0.i", "files"),
        ("printlib1.i", "files"),
        ("printlib3.i", "files"),
        ("printlib5.i", "files"),
        ("printlib7.i", "files"),
        ("printlib8.i", "files"),
        ("printlib9.i", "files"),
        ("simulation1.i", "files"),
        ("simulation2.i", "files"),
        ("simulation3.i", "files"),
        ("simulation4.i", "files"),
        ("simulation5.i", "files"),
        ("simulation5_ir.i", "files"),
        ("test121.i", "files"),
        ("test127.i", "files"),
    ],
    "Tst_709pt":
    [
        ("test141.i", "files"),
        ("test142.i", "files"),
        ("test143.i", "files"),
        ("test144.i", "files"),
    ],
    "Tst_mat":
    [
        ("collapse.i", "files"),
        ("condense.i", "files"),
        ("printlib.i", "files"),
        ("test.i", "files"),
        ("test1.i", "files"),
        ("test2.i", "files"),
        ("test3.i", "files"),
        ("test116.i", "files"),
    ],
    "Tst_nfy":
    [
        ("collapse.i", "files"),
        ("condense.i", "files"),
        ("printlib.i", "files"),
        ("test099.i", "files"),
        ("test100.i", "files"),
    ],
    "Tst_xray":
    [
        ("noxray.i", "files"),
        ("xray.i", "files"),
    ],
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-b",
        "--use-bin",
        help="Use binary data",
        action="store_true",
        default=False,
    )
    parser.add_argument("-o", "--output_file", required=False, default="results.json")
    args = parser.parse_args()

    output_file = args.output_file

    has_failure, all_results = runner.mp_run(TESTS, use_binary=args.use_bin)

    # write results to disk
    Path(output_file).write_text(json.dumps(all_results, indent=4, sort_keys=True))

    # check for errors
    if runner.check_all_errors(all_results) or has_failure:
        print("ERROR: Some tests failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
