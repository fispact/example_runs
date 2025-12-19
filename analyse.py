import argparse
from pathlib import Path
import json
from typing import Optional

import numpy as np


def create_prop_matrix_from_output(file_path: Path, prop: Optional[str] = "atoms", sorted_by: Optional[str] = "atoms", ntop: Optional[int] = 20) -> np.array:
    # we just take the top 20 nuclides by atoms per timestep
    # and construct a 3-d tensor for this.
    # nrofrows = 20, nrofcols = len(timesteps), nrofz = 3
    output_content = file_path.read_text()
    data = json.loads(output_content)

    inv_data = data['inventory_data']
    result = np.zeros(shape=(ntop, len(inv_data), 3))
    for j, timestep in enumerate(inv_data):
        nuclides = timestep['nuclides']

        irrad_time = timestep['irradiation_time']
        cool_time = timestep['cooling_time']
        total_time = irrad_time + cool_time

        sorted_nuclides = sorted(nuclides, key=lambda x: x[sorted_by])

        top_nuclides = sorted_nuclides[:ntop]
        result[:len(top_nuclides), j, 0] = [ x[prop] for x in top_nuclides ]
        result[:len(top_nuclides), j, 1] = [ x['zai'] for x in top_nuclides ]
        result[:, j, 2] = total_time

    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--results")
    args = parser.parse_args()

    results_content = Path(args.results).read_text()
    results = json.loads(results_content)

    test_suites = results.keys()

    for test_suite in test_suites:
        for k, v in results[test_suite].items():
            if not v["has_failure"]:
                out_file = Path(v["json_file"])
                matrix = create_prop_matrix_from_output(out_file, prop="atoms")
                print(matrix)


if __name__ == '__main__':
    main()
