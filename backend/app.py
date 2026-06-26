import os
from flask import Flask, request, jsonify
from flask_cors import CORS
# Hint: If you use TensorFlow/PyTorch, make sure they are imported here:
# import tensorflow as tf
# import torch

app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) so your frontend can talk to it safely
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    # 1. Structural Check: Ensure the incoming request has a file attached
    if 'file' not in request.files:
        return jsonify({'error': 'No file payload provided in request.'}), 400
        
    file = request.files['file']
    
    # 2. Structural Check: Ensure a file was actually selected
    if file.filename == '':
        return jsonify({'error': 'Empty file submission received.'}), 400

    try:
        # -----------------------------------------------------------------
        # [PLACEHOLDER FOR YOUR MODEL PREPROCESSING AND EXECUTION]
        # In a typical script, you would do something like:
        #   img = preprocess_image(file)
        #   raw_score = model.predict(img)[0][0] 
        # -----------------------------------------------------------------
        
        # Simulated raw model score matching your terminal logs (0.35331094)
        # Let's pretend the model returns a score close to 0.35
        # Where 1.0 = Absolutely Real, and 0.0 = Absolutely Fake
        raw_score = 0.3533109426498413 

        # 3. Dynamic Threshold Logic Fix:
        # If the score is greater or equal to 0.50, it is more likely to be REAL.
        if raw_score >= 0.50:
            prediction_result = "REAL"
            # Express closeness to 1.0 as a clean percentage
            formatted_confidence = round(raw_score * 100, 2)
        
        # If the score drops below 0.50, it means it's mathematically closer to FAKE!
        else:
            prediction_result = "FAKE"
            # Calculate the confidence of it being FAKE by looking at the inverse distance from 1.0
            # Example: 1.0 - 0.3533 = 0.6466 -> 64.67% confident that the image is FAKE
            formatted_confidence = round((1.0 - raw_score) * 100, 2)

        # 4. Print statement logs to your terminal console for local tracking
        print("\n=== ENGINE DETECTION AUDIT ===")
        print(f"File Processed: {file.filename}")
        print(f"Raw Value:      {raw_score}")
        print(f"Prediction:     {prediction_result}")
        print(f"Confidence:     {formatted_confidence}%")
        print("==============================\n")

        # 5. Send clean JSON keys back to your frontend script.js
        return jsonify({
            'prediction': prediction_result,
            'confidence': formatted_confidence
        })

    except Exception as e:
        print(f"Execution Error: {str(e)}")
        return jsonify({'error': f'Internal ML evaluation error: {str(e)}'}), 500

if __name__ == '__main__':
    # Runs your backend engine locally on port 5000
    app.run(port=5000, debug=True)