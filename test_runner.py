#!/usr/bin/python3
import unittest

loader = unittest.TestLoader()

test_suite = loader.discover(start_dir='tests', pattern='*.py')

all_tests = unittest.TestSuite(test_suite)

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(all_tests)
    if result.wasSuccessful():
        exit(0)
    else:
        exit(1)
