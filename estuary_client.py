import configparser
import os
import requests


class Estuary:
    base_url = "https://shuttle-4.estuary.tech"

    def __init__(self, config_file="./estuary.conf"):
        self.config_file = config_file
        self.api_key = self._parse_api_key()
        self.auth_header = self._get_auth_header()

    def _parse_api_key(self, section='DEFAULT'):
        config = configparser.ConfigParser()
        config.read(self.config_file)
        return config[section]['API_KEY']

    def _get_auth_header(self):
        return {"Authorization": "Bearer " + self.api_key}

    def list_data(self):
        resp = requests.get(url=Estuary.base_url + "/content/stats", headers=self._get_auth_header())
        if resp.status_code == 200:
            return resp.json()

    def add_data(self, data_dir, filename):
        with open(os.path.join(data_dir, filename), 'rb') as file:
            print("Uploading " + filename)
            resp = requests.post(
                url=Estuary.base_url + "/content/add",
                headers=self.auth_header,
                files={"data": file}
            )

        if resp.status_code == 200:
            print("Uploaded " + filename)
        else:
            print(resp.status_code)
            print(resp.json())

        return resp.status_code


estuary = Estuary()