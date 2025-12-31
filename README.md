# Autism Emotion Detection - Web Application

A beautiful web application for real-time emotion detection using AI, built with React, Tailwind CSS, and Flask.

## Features

- 🎥 Real-time emotion detection via webcam
- 📸 Image upload for emotion analysis
- 🎨 Modern, responsive UI with Tailwind CSS
- 🤖 Powered by DeepFace AI
- 📊 Detailed emotion breakdown with confidence scores
- 🚀 Fast and efficient API backend

## Dataset Information

This project uses the **FER (Facial Expression Recognition) Dataset** which includes 7 emotion categories:
- 😊 Happy
- 😢 Sad
- 😠 Angry
- 😲 Surprise
- 😨 Fear
- 🤢 Disgust
- 😐 Neutral

**Note:** For the web application, we use DeepFace which has pre-trained models, so no dataset download is required. However, if you want to train your own model using the scripts in the `scripts/` folder, you'll need to:

1. Download the FER dataset
2. Organize it in the following structure:
   ```
   data/
     train/
       Angry/
       Disgust/
       Fear/
       Happy/
       Sad/
       Surprise/
       Neutral/
     test/
       Angry/
       Disgust/
       Fear/
       Happy/
       Sad/
       Surprise/
       Neutral/
   ```

## Project Structure

```
Autism-Emotion-Detection/
├── backend/           # Flask API server
│   ├── app.py        # Main API application
│   └── requirements.txt
├── frontend/         # React application
│   ├── src/
│   ├── public/
│   └── package.json
├── scripts/          # Training and utility scripts
└── requirements.txt  # Main Python dependencies
```

## Installation

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Flask server:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The app will open at `http://localhost:3000`

## Usage

1. **Start the backend server** (Flask API)
2. **Start the frontend** (React app)
3. **Open your browser** to `http://localhost:3000`
4. Click "Start Camera" to begin real-time detection, or upload an image file

## API Endpoints

- `GET /api/health` - Health check endpoint
- `POST /api/detect-emotion` - Detect emotion from base64 image
- `POST /api/detect-emotion-file` - Detect emotion from uploaded file

## Technologies Used

- **Frontend:** React, Tailwind CSS, Axios
- **Backend:** Flask, Flask-CORS
- **AI/ML:** DeepFace, OpenCV, TensorFlow
- **Image Processing:** OpenCV, NumPy

## Development

To modify the frontend API URL, create a `.env` file in the `frontend/` directory:
```
REACT_APP_API_URL=http://localhost:5000
```

## License

This project is for educational purposes.

