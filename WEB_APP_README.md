# 🎭 Facial Emotion Detection Web Application

A beautiful web application for real-time facial emotion detection and mental health analysis using the trained Swin Transformer model.

## ✨ Features

- **Real-time Emotion Detection**: Analyze emotions from your webcam in real-time
- **Beautiful Neumorphism UI**: Soft, modern design using only black, white, and brown colors
- **Depression Risk Analysis**: Get mental health indicators based on detected emotions
- **Multi-face Detection**: Detect and analyze multiple faces simultaneously
- **Detailed Emotion Breakdown**: See probability scores for all 7 emotions
- **Responsive Design**: Works on desktop and mobile devices

## 🎨 UI Design

The web app features a **Neumorphism (Soft UI)** design with:

- **Primary Colors**: Black (#1a1a1a), White (#ffffff), Brown (#8B4513)
- **Soft shadows** for depth and dimension
- **Smooth animations** and transitions
- **Clean, modern interface**

## 📋 Prerequisites

Before running the web app, ensure you have:

1. ✅ Trained model at `Models/Swin_Transformer/best_model.pth`
2. ✅ Python 3.8 or higher installed
3. ✅ Webcam connected to your computer

## 🚀 Installation

### Step 1: Install Dependencies

```bash
pip install -r web_requirements.txt
```

Or install individually:

```bash
pip install Flask==2.3.2
pip install torch==2.0.0
pip install torchvision==0.15.0
pip install timm==0.9.2
pip install opencv-python==4.7.0.72
pip install Pillow==9.4.0
pip install numpy==1.23.5
```

### Step 2: Verify Model Exists

Make sure your trained model is located at:

```
Models/Swin_Transformer/best_model.pth
```

If you haven't trained the model yet, run:

```bash
python utilities/train_model.py
```

## 🎯 Running the Web App

### Start the Server

```bash
python web_app.py
```

You should see:

```
Loading model...
Using device: cuda (or cpu)
Model loaded successfully!

============================================================
Starting Flask Web Application
Open your browser and go to: http://localhost:5000
============================================================
```

### Access the Web App

1. Open your web browser
2. Navigate to: **http://localhost:5000**
3. Click **"Start Detection"** to begin
4. Allow camera permissions when prompted
5. Position your face in front of the camera

## 🎮 How to Use

### Starting Detection

1. Click the **"Start Detection"** button
2. Allow browser to access your camera
3. The app will automatically detect faces and analyze emotions

### Understanding Results

The app displays:

#### 1. **Detected Emotion**

- Primary emotion with confidence percentage
- Example: "Happy 89.3%"

#### 2. **Emotion Breakdown**

All 7 emotions with probability bars:

- Angry
- Disgust
- Fear
- Happy
- Neutral
- Sad
- Surprise

#### 3. **Mental Health Indicator**

Depression risk analysis:

- **Low Risk** (0-30%): Green indicator
- **Moderate Risk** (30-60%): Brown indicator
- **High Risk** (60-100%): Dark brown/red indicator

### Stopping Detection

Click **"Stop Detection"** to:

- Stop the camera
- Clear results
- Free up resources

## 🧠 Depression Risk Analysis

The app analyzes depression risk based on:

### Negative Emotion Indicators

- **Sad** (40% weight)
- **Fear** (30% weight)
- **Angry** (30% weight)

### Positive Emotion Indicators

- **Happy** (reduces risk)

### Risk Levels

- **Low (0-30%)**: Predominantly positive emotions
- **Moderate (30-60%)**: Mixed emotional state
- **High (60-100%)**: Predominantly negative emotions

⚠️ **Important**: This is an educational tool and should NOT replace professional medical advice or diagnosis.

## 🎨 UI Components

### Main Sections

1. **Header**

   - Title and description
   - Neumorphic styling

2. **Live Camera Feed**

   - Real-time video display
   - Face detection overlay
   - Brown bounding boxes around detected faces

3. **Analysis Results**

   - Emotion display cards
   - Probability bars
   - Depression risk indicator

4. **Footer**
   - Credits and disclaimer

### Color Scheme

```css
Background: #e0e0e0 (Light gray)
Text: #1a1a1a (Black)
Accent: #8B4513 (Brown)
Highlights: #ffffff (White)
```

## 🔧 Troubleshooting

### Camera Not Working

**Problem**: Camera access denied

**Solution**:

1. Check browser permissions
2. Allow camera access when prompted
3. Close other apps using the camera
4. Try a different browser (Chrome recommended)

### Model Not Found

**Problem**: "Model not found" error

**Solution**:

```bash
# Train the model first
python utilities/train_model.py
```

### Slow Performance

**Problem**: Detection is slow

**Solutions**:

1. **Use GPU**: The app automatically uses CUDA if available
2. **Close other apps**: Free up system resources
3. **Reduce detection frequency**: Edit `web_app.py` and change interval from 500ms to 1000ms

### No Face Detected

**Problem**: "No face detected" message

**Solutions**:

1. Ensure good lighting
2. Face the camera directly
3. Move closer to the camera
4. Remove obstructions (glasses, masks may affect detection)

## 📊 Technical Details

### Architecture

```
┌─────────────────┐
│   Frontend      │
│  (HTML/CSS/JS)  │
└────────┬────────┘
         │
         ↓ HTTP POST
┌─────────────────┐
│  Flask Server   │
│   (web_app.py)  │
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│  Swin Model     │
│  (PyTorch)      │
└─────────────────┘
```

### Detection Flow

1. **Capture**: JavaScript captures video frame
2. **Encode**: Convert to base64 JPEG
3. **Send**: POST to `/analyze_frame` endpoint
4. **Detect**: OpenCV detects faces
5. **Predict**: Swin Transformer predicts emotions
6. **Analyze**: Calculate depression risk
7. **Return**: Send results as JSON
8. **Display**: Update UI with results

### Performance

- **Detection Interval**: 500ms (2 FPS)
- **Image Quality**: 80% JPEG compression
- **Resolution**: 640x480 (ideal)
- **Processing Time**: ~100-300ms per frame (GPU)

## 🌐 Browser Compatibility

### Recommended Browsers

- ✅ Google Chrome (Latest)
- ✅ Microsoft Edge (Latest)
- ✅ Firefox (Latest)
- ✅ Safari (Latest)

### Required Features

- WebRTC (for camera access)
- Canvas API
- ES6 JavaScript
- Fetch API

## 🔒 Privacy & Security

### Data Handling

- ✅ All processing happens locally
- ✅ No data is stored on server
- ✅ No data is sent to external services
- ✅ Camera feed is not recorded

### Permissions

- Camera access required
- No microphone access needed
- No location access needed

## 📱 Mobile Support

The web app is responsive and works on mobile devices:

### Mobile Features

- Touch-friendly buttons
- Responsive layout
- Front/back camera selection
- Optimized for smaller screens

### Mobile Limitations

- May be slower on older devices
- Requires good lighting
- Battery consumption may be higher

## 🎓 Educational Use

This web app is designed for:

- Learning about emotion recognition
- Understanding AI/ML applications
- Demonstrating computer vision
- Educational demonstrations
- Research purposes

**Not suitable for**:

- Clinical diagnosis
- Medical decision-making
- Professional mental health assessment

## 🛠️ Customization

### Change Detection Interval

Edit `templates/index.html`:

```javascript
// Change from 500ms to 1000ms
detectionInterval = setInterval(detectEmotion, 1000);
```

### Modify Color Scheme

Edit CSS in `templates/index.html`:

```css
/* Change brown to another color */
.btn.active {
  background: #your-color;
}
```

### Adjust Depression Risk Algorithm

Edit `web_app.py`:

```python
def analyze_depression_risk(emotion_probs):
    # Modify weights and thresholds
    sad_score = emotion_probs[5] * 0.4  # Change weight
    # ... customize algorithm
```

## 📧 Support

For issues or questions:

- Check the troubleshooting section
- Review the main README.md
- Check HOW_TO_USE_MODEL.md
- Email: mujiyanto@amikom.ac.id

## 📄 License

Same license as the main project. See LICENSE file.

## 🙏 Credits

- **Model**: Swin Transformer
- **Dataset**: FER2013
- **Framework**: Flask, PyTorch
- **UI Design**: Neumorphism

---

**Happy Emotion Detecting! 😊**

Remember: This is an educational tool. Always consult healthcare professionals for mental health concerns.
