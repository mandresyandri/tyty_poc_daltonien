from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import requests
from io import BytesIO


class online_image:
    def __init__(self, url):
        self.url = url
        self.image = self._load_image()

    # Method load image
    def _load_image(self):
        try:
            response = requests.get(self.url)
            img = Image.open(BytesIO(response.content))
            return img
        except IOError:
            print("Impossible d'ouvrir l'image")
            return None

    # Convert image to np.array()
    def preprocess(self):
        if self.image is not None:
            return np.asarray(self.image)
        else:
            return None
