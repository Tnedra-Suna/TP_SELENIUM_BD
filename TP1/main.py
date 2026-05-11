"""
# main.py : appelle run_tests
"""

import sys, os
from tests.test_tp1 import run_tests

#Pour indiquer où chercher le dossier pages
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


if __name__ == "__main__":
    run_tests()
