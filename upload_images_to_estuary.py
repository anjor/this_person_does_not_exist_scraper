import os
from estuary_client import Estuary
from random_face_scraper import RandomFaceGenerator


def get_all_images(data_dir):
    return [image for image in os.listdir(data_dir) if not image.startswith(".")]


def upload_all_images(data_dir, api_key):
    estuary = Estuary(api_key)
    images = get_all_images(data_dir)
    for image in images:
        print("processing " + image)
        status = estuary.add_data(data_dir, image)
        if status == 200:
            os.remove(os.path.join(data_dir, image))


def upload_n_new_images(n, data_dir="./data", api_key=None):
    face_generator = RandomFaceGenerator()
    for i in range(n):
        face_generator.download_new_image()
        upload_all_images(data_dir, api_key)


def main():
    os.makedirs("./data", exist_ok=True)
    api_key = os.getenv("API_KEY")
    upload_n_new_images(100, api_key=api_key)


if __name__ == '__main__':
    main()
