#!/usr/bin/python3
import os
import sys

__unittest = True

# Insert lib in path, import testlib
sys.path.insert(0, os.path.join(os.path.os.path.dirname(
    os.path.os.path.abspath(__file__)), '..', 'lib'))
import testlib

class configLoadTestCase(testlib.SplunkConfTestCase):

    def test_configPresent(self):
        for config in self.configs:
            for item in self.configs[config]:
                self.assertTrue(
                    self.configs[config][item].sections(),
                    f'{config} {item} defined in SplunkConfUnitTests.yml is empty or does not exist',
                )

if __name__ == '__main__':
    import unittest
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)
