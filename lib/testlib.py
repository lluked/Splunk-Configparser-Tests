from __future__ import annotations

import argparse
import os
import unittest

import addonfactory_splunk_conf_parser_lib as SplunkConfigParser
import yaml


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('app_path', nargs=1, type=str, help='App Path')
    args = parser.parse_args()
    app_path = args.app_path[0]
    return app_path


def loadSplunkConfig(config_file):
    config = SplunkConfigParser.TABConfigParser()
    config.read(config_file)
    return config

# Custom unittest class for splunk configs


class SplunkConfTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app_dir = parseArgs()
        # Load test config
        with open(os.path.join(app_dir, 'SplunkConfUnitTests.yml')) as test_config_file:
            test_config = yaml.safe_load(test_config_file)
        # Create dict to hold splunk configs
        configs = {'default': {}, 'local': {}}
        # Load splunk configs
        for config in test_config:
            if config in ['default', 'local']:
                for item in test_config[config]:
                    configs[config][item] = loadSplunkConfig(
                        os.path.join(app_dir, config, item),
                    )
        # Assign to class to be accessible
        cls.configs = configs
