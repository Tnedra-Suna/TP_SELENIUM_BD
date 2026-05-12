import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from tests.test_search_products import run_test

if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
    
    