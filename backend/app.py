import os

from flask import Flask, request, jsonify
from predictor import predict_image

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return "DeepShield Backend Running"


@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return jsonify({
            "error": "No image uploaded"
        })

    file = request.files["image"]

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    result, confidence = predict_image(filepath)

    return jsonify({
        "prediction": result,
        "confidence": round(confidence * 100, 2)
    })


if __name__ == "__main__":
    app.run(debug=True)