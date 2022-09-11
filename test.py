"""
@Author: Fabian Kolesch

This file implements a test pipeline for the implemented snippets.
The tests will be run sequentially. If some test fails,
the pipeline is stopped.
"""

import test

if __name__ == "__main__":
    print("GENERATORS:")

    repeats = 1
    trials = 1000
    for i in range(repeats):
        test.ut_id_generator.stability(trials)