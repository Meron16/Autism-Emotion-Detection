from flask import Flask, request, jsonify
from flask_cors import CORS
from deepface import DeepFace
import cv2
import numpy as np
import base64
import os

app = Flask(__name__)
CORS(app)

# Emotion labels
EMOTION_LABELS = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "message": "Emotion Detection API is running"})

@app.route('/api/detect-emotion', methods=['POST'])
def detect_emotion():
    try:
        data = request.json
        
        if 'image' not in data:
            return jsonify({"error": "No image provided"}), 400
        
        # Decode base64 image
        image_data = data['image'].split(',')[1] if ',' in data['image'] else data['image']
        image_bytes = base64.b64decode(image_data)
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if img is None:
            return jsonify({"error": "Invalid image data"}), 400
        
        # Analyze emotion using DeepFace
        result = DeepFace.analyze(
            img, 
            actions=['emotion'],
            enforce_detection=False,
            silent=True
        )
        
        # Extract emotion data
        if isinstance(result, list):
            result = result[0]
        
        emotion_scores = result.get('emotion', {})
        dominant_emotion = result.get('dominant_emotion', 'Unknown')
        
        # Format response
        response = {
            "dominant_emotion": dominant_emotion,
            "emotions": emotion_scores,
            "confidence": emotion_scores.get(dominant_emotion, 0) if emotion_scores else 0
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/detect-emotion-file', methods=['POST'])
def detect_emotion_file():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file provided"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        
        # Read image file
        file_bytes = file.read()
        nparr = np.frombuffer(file_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if img is None:
            return jsonify({"error": "Invalid image file"}), 400
        
        # Analyze emotion using DeepFace
        result = DeepFace.analyze(
            img,
            actions=['emotion'],
            enforce_detection=False,
            silent=True
        )
        
        # Extract emotion data
        if isinstance(result, list):
            result = result[0]
        
        emotion_scores = result.get('emotion', {})
        dominant_emotion = result.get('dominant_emotion', 'Unknown')
        
        # Format response
        response = {
            "dominant_emotion": dominant_emotion,
            "emotions": emotion_scores,
            "confidence": emotion_scores.get(dominant_emotion, 0) if emotion_scores else 0
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True, use_reloader=False)

