import numpy as np
from PIL import Image


def preprocess_image(image_path):
    """
    Loads an uploaded image and prepares it
    for the MobileNetV2 model.
    """

    image = Image.open(image_path)

    image = image.convert("RGB")

    image = image.resize((224, 224))

    image = np.array(image)

    image = image / 255.0

    image = np.expand_dims(image, axis=0)

    return image