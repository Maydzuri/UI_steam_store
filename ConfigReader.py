import json


class ConfigReader:
    def __init__(self, config_file='config.json'):
        with open(config_file, 'r') as file:
            self.config_data = json.load(file)

    def get(self, key):
        return self.config_data.get(key)
