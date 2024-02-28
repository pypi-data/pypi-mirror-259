import unittest
from algojig import coverage

if __name__ == "__main__":

    unittest.main(module="tests", exit=False)
    for p in coverage.coverage:
        print(f"Coverage {p.filename}")
        coverage.report_coverage(p)
