import json


class ConfigReader:
    DEFAULT_CONFIG_PATH = 'config.json'  # Константа на уровне класса

    def __init__(self, config_file=None):
        if config_file is None:
            config_file = self.DEFAULT_CONFIG_PATH

        with open(config_file, 'r') as file:
            self.config_data = json.load(file)

    def get(self, key):
        return self.config_data.get(key)
