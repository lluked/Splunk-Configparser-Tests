#!/usr/bin/python3
import os
import sys
import json
from jsonschema import validate

__unittest = True

# Insert lib in path, import testlib
sys.path.insert(0, os.path.join(os.path.os.path.dirname(
    os.path.os.path.abspath(__file__)), '..', 'lib'))
import testlib

class schemaTestCase(testlib.SplunkConfTestCase):

    def test_schema(self):
        for config in self.configs:
            # print(config)
            for item in self.configs[config]:
                config_config = self.configs[config][item]
                with open('schema/{}.json'.format(item.split(".")[0])) as schema_file:
                    schema = json.load(schema_file)
                    # print(json.dumps(schema, indent=4))
                    for section in config_config:
                        if section not in ['DEFAULT','ERROR']:
                            instance = dict((config_config[section]))
                            validate(instance=instance, schema=schema)

if __name__ == '__main__':
    import unittest
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)
