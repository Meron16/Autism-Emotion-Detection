import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load model
model = load_model('models/model.h5')
emotion_labels = ['Angry','Disgust','Fear','Happy','Sad','Surprise','Neutral']

# Start webcam
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        roi = gray[y:y+h, x:x+w]
        roi = cv2.resize(roi, (48,48))
        roi = roi/255.0
        roi = np.expand_dims(roi, axis=0)
        roi = np.expand_dims(roi, axis=-1)
        pred = model.predict(roi)
        label = emotion_labels[np.argmax(pred)]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(frame,label,(x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,(0,255,0),2)
    cv2.imshow('Emotion Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
