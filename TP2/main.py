import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tests.test_tp2 import run_tests

if __name__ == "__main__":
    run_tests()