import os
import tensorflow as tf

from utils import preprocess_image

# Path to the trained model
MODEL_PATH = os.path.join(
    "..",
    "model",
    "deepshield_mobilenetv2.keras"
)

# Load the model only once when the backend starts
model = tf.keras.models.load_model(MODEL_PATH)


def predict_image(image_path):
    """
    Predict whether an image is REAL or FAKE.
    """

    # Preprocess the uploaded image
    image = preprocess_image(image_path)

    # Get prediction
    prediction = model.predict(image, verbose=0)

    # Confidence score (between 0 and 1)
    confidence = float(prediction[0][0])

    # Decide the class
    if confidence >= 0.5:
        result = "FAKE"
    else:
        result = "REAL"

    return result, confidence