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
        ## Load config types defined in test config and iterate over (default/local)
        for config_type in self.configs:
            # print(config_type)
            ## Load configs in config_type and iterate over (transforms.conf, collections.conf, etc.)
            for config in self.configs[config_type]:
                # print(config)
                ## Load actual config_item and process
                config_item = self.configs[config_type][config]
                # print(config_item)
                with open('schema/{}.json'.format(config.split('.')[0])) as schema_file:
                    config_schema = json.load(schema_file)
                    # print(json.dumps(schema, indent=4))
                    for section in config_item:
                        ## Ignore configparser DEFAULT and ERROR sections
                        if section not in ['DEFAULT','ERROR']:
                            # print(config_item[section])
                            ## Load section into dict for schema validation
                            config_instance = dict((config_item[section]))
                            # print(json.dumps(config_instance, indent=4))
                            ## Validate config against schema
                            validate(instance=config_instance, schema=config_schema)

if __name__ == '__main__':
    import unittest
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)
