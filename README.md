# DeepShield

AI-Powered Deepfake Detection Platform

## Project Description

DeepShield is a cybersecurity and data science project designed to detect manipulated images and videos using deep learning techniques.

## Technologies

- Python
- TensorFlow
- OpenCV
- FastAPI
- React
- GitHub
- # DeepShield – AI Powered Deepfake Detection Platform

> Detect manipulated facial images using Deep Learning and MobileNetV2.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![HTML](https://img.shields.io/badge/HTML-Frontend-red)
![CSS](https://img.shields.io/badge/CSS-Styling-blue)
![JavaScript](https://img.shields.io/badge/JavaScript-Interactive-yellow)

---

# Overview

DeepShield is an AI-powered web application that detects whether a facial image is **Real** or **Deepfake** using a Convolutional Neural Network based on **MobileNetV2 Transfer Learning**.

Users can upload an image through a modern web interface, and the application predicts whether the uploaded image has been manipulated, along with a confidence score.

This project combines **Artificial Intelligence**, **Computer Vision**, and **Full Stack Web Development** into a complete end-to-end application.

---

# Features

- Upload any facial image
- Detect Real vs Deepfake images
- MobileNetV2 Transfer Learning model
- Confidence score for every prediction
- Flask REST API backend
- Responsive web interface
- Image preview before prediction
- Fast inference using TensorFlow
- Modular project structure

---

# Model Architecture

The deep learning model is built using **Transfer Learning**.

### Base Model

- MobileNetV2 (ImageNet Weights)

### Classification Head

- GlobalAveragePooling2D
- Dense Layer (128 Neurons, ReLU)
- Dropout Layer
- Output Layer (Sigmoid)

The MobileNetV2 base model was initially frozen and trained with a custom classifier for binary classification.

---

# Model Performance

| Metric | Score |
|---------|------:|
| Test Accuracy | **60%** |
| Precision | **61%** |
| Recall | **60%** |
| F1 Score | **60%** |

### Confusion Matrix

| | Predicted Real | Predicted Fake |
|---|---:|---:|
| Actual Real | 126 | 91 |
| Actual Fake | 73 | 119 |

*(Update these values if you retrain your model.)*

---

# Technologies Used

### Artificial Intelligence

- TensorFlow
- Keras
- MobileNetV2
- NumPy

### Backend

- Flask
- Flask-CORS

### Frontend

- HTML5
- CSS3
- JavaScript

### Development

- Python
- VS Code
- Git
- GitHub

---

# Project Structure

```
DeepShield/
│
├── backend/
│   ├── app.py
│   ├── predictor.py
│   ├── utils.py
│   ├── uploads/
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── model/
│   └── deepshield_mobilenetv2.keras
│
├── notebooks/
│   ├── 01_dataset_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_mobilenetv2_training.ipynb
│
├── dataset/
├── .gitignore
├── README.md
└── requirements.txt
```

---

# Installation

Clone the repository.

```bash
git clone https://github.com/gnapiika/DeepShield-Deepfake-Detection.git
```

Go into the project directory.

```bash
cd DeepShield-Deepfake-Detection
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Running the Backend

Navigate to the backend folder.

```bash
cd backend
```

Run the Flask server.

```bash
python app.py
```

Backend runs at:

```
http://127.0.0.1:5000
```

---

# Running the Frontend

Open the **frontend** folder.

Launch **index.html** using the Live Server extension in VS Code.

The frontend communicates with the Flask backend automatically.

---

# How It Works

1. User uploads an image.
2. Frontend sends the image to the Flask API.
3. Backend preprocesses the image.
4. MobileNetV2 performs inference.
5. Prediction is returned as:
   - REAL
   - FAKE
6. Confidence score is displayed.

---

# Workflow

```
User
   │
   ▼
Upload Image
   │
   ▼
Frontend (HTML/CSS/JS)
   │
   ▼
Flask API
   │
   ▼
Image Preprocessing
   │
   ▼
MobileNetV2 Model
   │
   ▼
Prediction
   │
   ▼
Confidence Score
   │
   ▼
Display Result
```

---

# Screenshots

## Home Page

<img width="842" height="755" alt="image" src="https://github.com/user-attachments/assets/392f2117-eb58-4baf-b5cd-a8c2dc0f9f57" />


---

## Image Uploaded

<img width="927" height="777" alt="image" src="https://github.com/user-attachments/assets/7e3ebd53-efe0-4773-877e-0af2eafc4b10" />


---

## Prediction Result

<img width="748" height="903" alt="image" src="https://github.com/user-attachments/assets/59876d32-d3c2-4f8f-9aa4-5297eb5df8fb" />


---

# Future Improvements

- Fine-tune MobileNetV2 layers
- Support video deepfake detection
- Explainable AI (Grad-CAM)
- Face detection before classification
- Batch image prediction
- User authentication
- Prediction history
- Cloud deployment
- Docker support
- Mobile application

---

# Learning Outcomes

This project demonstrates practical experience in:

- Deep Learning
- Transfer Learning
- Computer Vision
- TensorFlow
- Flask API Development
- Frontend Development
- REST APIs
- Model Deployment
- Git & GitHub
- End-to-End AI Application Development

---

# Author

**Gnapika Reddy**

B.Tech Computer Science Engineering

Specializations:

- Cybersecurity
- Artificial Intelligence
- Data Science
- Full Stack Development
- Game Development

GitHub:
https://github.com/gnapiika

LinkedIn:
https://linkedin.com/in/gnapiika

---

