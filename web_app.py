"""
Flask Web Application for Facial Emotion Detection
Real-time emotion detection with depression analysis
"""

import os
import cv2
import torch
import timm
import numpy as np
from flask import Flask, render_template, Response, jsonify
from torchvision import transforms
from PIL import Image
import base64
from io import BytesIO

app = Flask(__name__)

class CustomSwinTransformer(torch.nn.Module):
    def __init__(self, pretrained=True, num_classes=7):
        super(CustomSwinTransformer, self).__init__()
        self.backbone = timm.create_model('swin_base_patch4_window7_224', pretrained=pretrained, num_classes=0)
        self.classifier = torch.nn.Sequential(
            torch.nn.Linear(self.backbone.num_features, 512),
            torch.nn.ReLU(),
            torch.nn.Dropout(p=0.6),
            torch.nn.Linear(512, num_classes)
        )

    def forward(self, x):
        x = self.backbone(x)
        return self.classifier(x)

# Global variables
model = None
device = None
transform = None
face_cascade = None
emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

def load_model():
    """Load the trained model"""
    global model, device, transform, face_cascade
    
    model_path = "Models/Swin_Transformer/best_model.pth"
    
    if not os.path.exists(model_path):
        print(f"Error: Model not found at {model_path}")
        return False
    
    print("Loading model...")
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")
    
    model = CustomSwinTransformer(pretrained=False, num_classes=7)
    model.load_state_dict(torch.load(model_path, map_location=device), strict=False)
    model = model.to(device)
    model.eval()
    
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    print("Model loaded successfully!")
    return True

def analyze_depression_risk(emotion_probs):
    """
    Analyze depression risk based on emotion probabilities
    Returns risk level and percentage
    """
    # Depression indicators: sad, fear, angry (negative emotions)
    # Positive indicators: happy, surprise
    
    sad_score = emotion_probs[5]  # Sad
    fear_score = emotion_probs[2]  # Fear
    angry_score = emotion_probs[0]  # Angry
    happy_score = emotion_probs[3]  # Happy
    
    # Calculate depression risk (0-100)
    negative_emotions = (sad_score * 0.4 + fear_score * 0.3 + angry_score * 0.3)
    positive_emotions = happy_score
    
    # Risk calculation
    depression_risk = (negative_emotions * 100) - (positive_emotions * 20)
    depression_risk = max(0, min(100, depression_risk))  # Clamp between 0-100
    
    # Determine risk level
    if depression_risk < 30:
        risk_level = "Low"
        color = "#8B4513"  # Brown
    elif depression_risk < 60:
        risk_level = "Moderate"
        color = "#A0522D"  # Sienna
    else:
        risk_level = "High"
        color = "#654321"  # Dark brown
    
    return {
        'risk_level': risk_level,
        'risk_percentage': round(depression_risk, 1),
        'color': color
    }

def process_frame(frame):
    """Process a single frame and return emotion predictions"""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    
    results = []
    
    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        
        try:
            # Convert to PIL Image and preprocess
            face_pil = Image.fromarray(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))
            face_tensor = transform(face_pil).unsqueeze(0).to(device)
            
            # Make prediction
            with torch.no_grad():
                output = model(face_tensor)
                probabilities = torch.nn.functional.softmax(output, dim=1)
                confidence, predicted = torch.max(probabilities, 1)
            
            emotion = emotions[predicted.item()]
            conf = confidence.item()
            probs = probabilities[0].cpu().numpy()
            
            # Analyze depression risk
            depression_analysis = analyze_depression_risk(probs)
            
            results.append({
                'emotion': emotion,
                'confidence': round(conf * 100, 1),
                'probabilities': {emotions[i]: round(float(probs[i]) * 100, 1) for i in range(len(emotions))},
                'depression': depression_analysis,
                'bbox': {'x': int(x), 'y': int(y), 'w': int(w), 'h': int(h)}
            })
        
        except Exception as e:
            print(f"Error processing face: {e}")
            continue
    
    return results

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/analyze_frame', methods=['POST'])
def analyze_frame():
    """Analyze a frame from the webcam"""
    from flask import request
    
    try:
        # Get image data from request
        data = request.get_json()
        image_data = data['image'].split(',')[1]
        
        # Decode base64 image
        image_bytes = base64.b64decode(image_data)
        nparr = np.frombuffer(image_bytes, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Process frame
        results = process_frame(frame)
        
        return jsonify({
            'success': True,
            'results': results
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    if load_model():
        print("\n" + "="*60)
        print("Starting Flask Web Application")
        print("Open your browser and go to: http://localhost:5000")
        print("="*60 + "\n")
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        print("Failed to load model. Please train the model first.")
