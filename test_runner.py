#!/usr/bin/python3
import unittest
import os

loader = unittest.TestLoader()

tests_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tests')

test_suite = loader.discover(start_dir=tests_path, pattern='*.py')

all_tests = unittest.TestSuite(test_suite)

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(all_tests)
    if result.wasSuccessful():
        exit(0)
    else:
        exit(1)
