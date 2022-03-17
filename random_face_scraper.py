import requests as re
import shutil


class RandomFaceGenerator:
    data_dir = "./data/"

    def __init__(self):
        self.images = []

    def download_new_image(self):
        resp = re.get(url="https://www.this-person-does-not-exist.com/en?new")
        resp = resp.json()
        self.images.append(resp['name'])

        self._download_image()

    def _download_image(self):
        image = self.images.pop()
        resp = re.get(url="https://www.this-person-does-not-exist.com/img/" + image, stream=True)

        if resp.status_code == 200:
            with open(image, 'wb') as f:
                shutil.copyfileobj(resp.raw, f)
            shutil.move(image, RandomFaceGenerator.data_dir + image)

    def download_all_images(self):
        while self.images:
            self._download_image()





