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

    # Probability that the image is FAKE
    fake_probability = float(prediction[0][0])

    # Determine prediction and confidence
    if fake_probability >= 0.5:
        result = "FAKE"
        confidence = fake_probability
    else:
        result = "REAL"
        confidence = 1 - fake_probability

    return result, confidence