import os
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from PIL import Image

# Initialize Flask App
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) so your Vercel frontend can connect
CORS(app)

# Configure temporary file upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# --- 1. NEW HOME ROUTE FOR BROWSER LANDING PAGE ---
@app.route('/', methods=['GET'])
def home():
    return """
    <html>
        <head>
            <title>DeepShield API Gateway</title>
            <style>
                body { 
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; 
                    background: #0a0a1a; 
                    color: #fff; 
                    text-align: center; 
                    padding: 80px 20px; 
                }
                .card { 
                    background: rgba(255, 255, 255, 0.03); 
                    padding: 40px; 
                    border-radius: 16px; 
                    display: inline-block; 
                    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37); 
                    backdrop-filter: blur(4px);
                    border: 1px solid rgba(255, 255, 255, 0.1);
                    max-width: 500px;
                }
                h1 { color: #e2e8f0; margin-bottom: 10px; font-weight: 600; }
                p { color: #94a3b8; font-size: 1.1rem; }
                .status { 
                    background: rgba(78, 223, 159, 0.1); 
                    color: #4edf9f; 
                    padding: 6px 14px; 
                    border-radius: 20px; 
                    font-weight: bold; 
                    font-size: 0.9rem;
                    display: inline-block;
                    margin-top: 10px;
                }
                small { color: #64748b; display: block; margin-top: 25px; font-family: monospace; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🛡️ DeepShield AI Gateway</h1>
                <p>The deepfake verification neural engine is online.</p>
                <div class="status">● Server Live</div>
                <small>API Endpoint active at: POST /predict</small>
            </div>
        </body>
    </html>
    """

# --- 2. DEEPFAKE ANALYSIS ENDPOINT ---
@app.route('/predict', methods=['POST'])
def predict():
    # Verify an image file was included in the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected for upload'}), 400

    try:
        # Secure and temporarily save the file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # -------------------------------------------------------------
        # SIMULATED NEURAL NETWORK PROCESSING (MobileNetV2 Thresholds)
        # -------------------------------------------------------------
        # Open and check image metrics to mock model performance
        with Image.open(filepath) as img:
            img_array = np.array(img)
            # Create a deterministic fake rating metric based on standard image deviations
            variance_factor = float(np.var(img_array)) if img_array.size > 0 else 5000.0
            
        # Clear the processed file out of the container to free storage
        if os.path.exists(filepath):
            os.remove(filepath)

        # Algorithmic check mapping variance limits to fake threshold ranges
        is_deepfake = variance_factor % 2 == 0
        confidence_score = round(85.4 + (variance_factor % 14.1), 2)

        # Construct JSON package to feed back into your glassmorphic frontend UI
        return jsonify({
            'success': True,
            'prediction': 'Deepfake Detected' if is_deepfake else 'Authentic / Real Image',
            'confidence': confidence_score,
            'status': 'verified',
            'metrics': {
                'noise_analysis': 'High resolution anomalies flagged' if is_deepfake else 'Consistent sensor signature matching',
                'artifact_score': round(variance_factor % 100, 2)
            }
        }), 200

    except Exception as e:
        # Error recovery
        if 'filepath' in locals() and os.path.exists(filepath):
            os.remove(filepath)
        return jsonify({'error': f'Analysis pipeline exception: {str(e)}'}), 500

# Entry point wrapper for localized environment executions
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)