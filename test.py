"""
@Author: Fabian Kolesch

This file implements a test pipeline for the implemented snippets.
The tests run sequentially.
"""

import test

if __name__ == "__main__":
    print("GENERATORS:")
    trials = 10000

    test.ut_id_generator.stability(trials)
