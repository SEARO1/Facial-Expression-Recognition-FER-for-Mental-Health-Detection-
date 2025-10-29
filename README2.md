# 🚀 Complete Setup Guide for Facial Expression Recognition (FER) Project

## 📋 Table of Contents
1. [System Requirements](#system-requirements)
2. [Prerequisites Installation](#prerequisites-installation)
3. [Project Setup (Step-by-Step)](#project-setup-step-by-step)
4. [Downloading the Pre-trained Model](#downloading-the-pre-trained-model)
5. [Running the Web Application](#running-the-web-application)
6. [Troubleshooting Common Issues](#troubleshooting-common-issues)
7. [Using the Web Application](#using-the-web-application)
8. [Training Your Own Model (Advanced)](#training-your-own-model-advanced)
9. [Project Structure Explained](#project-structure-explained)
10. [FAQ](#faq)

---

## 🖥️ System Requirements

### Minimum Requirements:
- **Operating System**: Windows 10/11, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **RAM**: 8GB (16GB recommended)
- **Storage**: 2GB free space
- **Processor**: Intel i5 or equivalent (Intel i7 or AMD Ryzen recommended)
- **Webcam**: Built-in or USB webcam for real-time detection
- **Internet**: Required for downloading model and dependencies

### Optional (for GPU acceleration):
- **GPU**: NVIDIA GPU with CUDA support (GTX 1060 or better)
- **VRAM**: 4GB+ GPU memory
- **CUDA**: Version 11.0 or higher

---

## 📥 Prerequisites Installation

### Step 1: Install Python

#### Windows:
1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download Python 3.10 or 3.11 (recommended)
3. **IMPORTANT**: Check "Add Python to PATH" during installation
4. Click "Install Now"
5. Verify installation:
   ```powershell
   python --version
   ```
   You should see: `Python 3.10.x` or `Python 3.11.x`

#### macOS:
```bash
# Install Homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.11

# Verify installation
python3 --version
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip
python3 --version
```

### Step 2: Install Git

#### Windows:
1. Download from [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Run installer with default settings
3. Verify:
   ```powershell
   git --version
   ```

#### macOS:
```bash
brew install git
git --version
```

#### Linux:
```bash
sudo apt install git
git --version
```

---

## 🔧 Project Setup (Step-by-Step)

### Step 1: Clone the Repository

Open your terminal (PowerShell on Windows, Terminal on macOS/Linux):

```bash
# Navigate to your desired directory
cd Desktop
# or
cd Documents

# Clone the repository
git clone https://github.com/SEARO1/Facial-Expression-Recognition-FER-for-Mental-Health-Detection-.git

# Navigate into the project folder
cd Facial-Expression-Recognition-FER-for-Mental-Health-Detection-
```

**Expected Result**: You should now be inside the project directory.

### Step 2: Create a Virtual Environment

A virtual environment isolates your project dependencies from other Python projects.

#### Windows (PowerShell):
```powershell
# Create virtual environment
python -m venv .venv

# Activate the virtual environment
.\.venv\Scripts\Activate.ps1

# If you get an error about execution policy, run this first:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Windows (Command Prompt):
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

#### macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Expected Result**: Your terminal prompt should now show `(.venv)` at the beginning, indicating the virtual environment is active.

Example:
```
(.venv) PS C:\Users\YourName\Desktop\Facial-Expression-Recognition-FER-for-Mental-Health-Detection->
```

### Step 3: Install Required Dependencies

Now install all the necessary Python packages:

```bash
# Upgrade pip first (important!)
python -m pip install --upgrade pip

# Install web application dependencies
pip install -r web_requirements.txt
```

**This will install**:
- Flask 2.3.2 (web framework)
- PyTorch 2.0.0 (deep learning framework)
- torchvision 0.15.0 (computer vision tools)
- timm 0.9.2 (pre-trained models)
- opencv-python 4.7.0.72 (computer vision)
- Pillow 9.4.0 (image processing)
- numpy 1.23.5 (numerical computing)

**Installation Time**: 5-10 minutes depending on your internet speed.

**Expected Output**:
```
Successfully installed Flask-2.3.2 torch-2.0.0 torchvision-0.15.0 timm-0.9.2 ...
```

### Step 4: Verify Installation

Check if all packages are installed correctly:

```bash
pip list
```

You should see all the packages listed above.

---

## 📦 Downloading the Pre-trained Model

The trained model file is hosted on Hugging Face (not included in GitHub due to its large size ~400MB).

### Option 1: Interactive Download (Recommended for Beginners)

```bash
python download_model.py
```

**Follow the prompts**:
1. The script will ask: `Enter your Hugging Face repository ID:`
2. Type: `SEARO1/FER_model` (or the repository ID provided by your team)
3. Press Enter
4. Wait for the download to complete (5-10 minutes)

**Expected Output**:
```
======================================================================
Facial Expression Recognition Model - Download from Hugging Face
======================================================================

📦 Model Repository Information
----------------------------------------------------------------------
Enter your Hugging Face repository ID: SEARO1/FER_model

🔄 Downloading model from: SEARO1/FER_model
This may take a few minutes depending on your internet connection...
----------------------------------------------------------------------

======================================================================
🎉 SUCCESS! Model downloaded successfully!
======================================================================

📍 Model saved to: Models\Swin_Transformer\best_model.pth
📊 Model size: 400.25 MB

✅ You can now run the web application with: python web_app.py
```

### Option 2: Manual Download

If the script doesn't work:

1. Go to the Hugging Face repository: [https://huggingface.co/SEARO1/FER_model](https://huggingface.co/SEARO1/FER_model)
2. Click on "Files and versions"
3. Download `best_model.pth`
4. Create folders: `Models\Swin_Transformer\`
5. Move the downloaded file to: `Models\Swin_Transformer\best_model.pth`

### Verify Model Download

Check if the model file exists:

#### Windows (PowerShell):
```powershell
Test-Path Models\Swin_Transformer\best_model.pth
```
Should return: `True`

#### macOS/Linux:
```bash
ls -lh Models/Swin_Transformer/best_model.pth
```
Should show the file size (~400MB)

---

## 🌐 Running the Web Application

### Step 1: Start the Flask Server

Make sure your virtual environment is activated (you should see `(.venv)` in your prompt).

```bash
python web_app.py
```

**Expected Output**:
```
Loading model...
Using device: cpu
Model loaded successfully!

============================================================
Starting Flask Web Application
Open your browser and go to: http://localhost:5000
============================================================

 * Serving Flask app 'web_app'
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.100.18:5000
Press CTRL+C to quit
 * Debugger is active!
```

**What's happening**:
- The model is being loaded into memory (~3-5 seconds)
- Flask starts a local web server
- The application is accessible at multiple URLs

### Step 2: Open the Web Application

1. Open your web browser (Chrome, Firefox, Edge, or Safari)
2. Go to: **http://localhost:5000**
   
   Alternative URLs if localhost doesn't work:
   - http://127.0.0.1:5000
   - http://192.168.100.18:5000 (or the IP shown in your terminal)

### Step 3: Grant Camera Permissions

When you first open the application:

1. Your browser will ask for camera permissions
2. Click **"Allow"** or **"Yes"** to grant access
3. The webcam feed should appear in the left panel

**Browser-specific notes**:
- **Chrome/Edge**: Permission popup appears at the top
- **Firefox**: Permission popup appears at the left of address bar
- **Safari**: Permission dialog appears in the center

---

## 🎯 Using the Web Application

### Interface Overview

The web application has several sections:

```
┌─────────────────────────────────────────────────────────┐
│  Facial Emotion & Depression Detection                  │
│  Real-time AI-powered mental health monitoring          │
├──────────────────────┬──────────────────────────────────┤
│                      │                                  │
│   📹 Webcam Feed     │    😊 Emotion Analysis          │
│   (Real-time video)  │    (Current detected emotion)   │
│                      │                                  │
├──────────────────────┼──────────────────────────────────┤
│                      │                                  │
│   🧠 Depression Risk │    📊 Emotion Probabilities     │
│   (Risk level)       │    (Bar chart of all emotions)  │
│                      │                                  │
└──────────────────────┴──────────────────────────────────┘
```

### Features Explained

#### 1. Real-time Emotion Detection
- **7 Emotion Classes**:
  - 😠 Angry
  - 🤢 Disgust
  - 😨 Fear
  - 😊 Happy
  - 😐 Neutral
  - 😢 Sad
  - 😲 Surprise

#### 2. Confidence Scores
- Shows how confident the AI is about the detected emotion
- Range: 0-100%
- Higher is better (>70% is considered reliable)

#### 3. Depression Risk Analysis
The system analyzes emotional patterns:
- **Low Risk** (0-30%): Predominantly positive emotions
- **Moderate Risk** (30-60%): Mixed emotional patterns
- **High Risk** (60-100%): Predominantly negative emotions

**Note**: This is not a medical diagnosis. Always consult a mental health professional.

#### 4. Emotion Probability Distribution
Shows the likelihood of all 7 emotions in real-time:
```
Happy:    ████████████ 85%
Sad:      ███ 8%
Angry:    ██ 3%
Neutral:  ██ 2%
Surprise: █ 1%
Fear:     █ 0.5%
Disgust:  █ 0.5%
```

### How to Use

1. **Position yourself**: Sit 1-2 feet from the camera
2. **Good lighting**: Ensure your face is well-lit
3. **Face the camera**: Look directly at the webcam
4. **Wait for detection**: Green box appears around detected faces
5. **View results**: Emotion and depression risk update in real-time

### Tips for Best Results

✅ **DO**:
- Use good lighting (natural or bright indoor light)
- Keep your face visible and unobstructed
- Maintain a neutral expression initially
- Be at a comfortable distance (1-2 feet)

❌ **DON'T**:
- Cover your face with hands or objects
- Use in very dark environments
- Move too quickly or erratically
- Have multiple faces in frame simultaneously

---

## 🔧 Troubleshooting Common Issues

### Issue 1: "Python is not recognized"

**Problem**: Terminal says `python is not recognized as a command`

**Solution**:
1. Reinstall Python and check "Add Python to PATH"
2. Or use full path: `C:\Users\YourName\AppData\Local\Programs\Python\Python311\python.exe`
3. On Windows, try `py` instead of `python`

### Issue 2: "Cannot activate virtual environment"

**Problem**: `.venv\Scripts\Activate.ps1` gives an execution policy error

**Solution** (Windows PowerShell):
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then try activating again.

### Issue 3: "Model not found"

**Problem**: `Error: Model not found at Models/Swin_Transformer/best_model.pth`

**Solution**:
1. Check if the model file exists:
   ```powershell
   ls Models\Swin_Transformer\
   ```
2. If missing, re-download:
   ```bash
   python download_model.py
   ```
3. Verify file size is ~400MB (not 0 bytes)

### Issue 4: "Connection refused" in browser

**Problem**: Browser shows "ERR_CONNECTION_REFUSED" or "Unable to connect"

**Solutions**:
1. **Check if server is running**:
   - Look for "Running on http://127.0.0.1:5000" in terminal
   - If not, restart: `python web_app.py`

2. **Try different URLs**:
   - http://localhost:5000
   - http://127.0.0.1:5000

3. **Clear browser cache**:
   - Press `Ctrl + Shift + Delete`
   - Clear cached images and files
   - Or use Incognito/Private mode

4. **Check firewall**:
   - Windows Firewall might be blocking port 5000
   - Allow Python in Windows Defender Firewall

5. **Port already in use**:
   ```bash
   # Stop the running process
   # Press Ctrl+C in the terminal running web_app.py
   # Then restart: python web_app.py
   ```

### Issue 5: "Camera not working"

**Problem**: Webcam feed shows black screen or "No camera detected"

**Solutions**:
1. **Check camera permissions**:
   - Browser settings → Privacy → Camera
   - Allow access for localhost

2. **Camera in use by another app**:
   - Close Zoom, Teams, Skype, or other video apps
   - Restart your browser

3. **Test camera**:
   - Windows: Open Camera app
   - macOS: Open Photo Booth
   - Linux: Open Cheese

4. **Update webcam drivers** (Windows):
   - Device Manager → Cameras → Right-click → Update driver

### Issue 6: Slow performance

**Problem**: Application is laggy or slow

**Solutions**:
1. **Close other applications**:
   - Free up RAM and CPU
   - Close unnecessary browser tabs

2. **Lower resolution**:
   - Move closer to camera for better detection
   - Application will process smaller face regions faster

3. **Use GPU** (if available):
   - Install CUDA-enabled PyTorch:
   ```bash
   pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
   ```

### Issue 7: "CUDA out of memory"

**Problem**: Error about GPU memory on systems with NVIDIA GPU

**Solution**:
The application automatically falls back to CPU. This is normal and expected.

### Issue 8: Incorrect emotion detection

**Problem**: AI detects wrong emotions consistently

**Solutions**:
1. **Improve lighting**: Face should be evenly lit
2. **Check camera quality**: Clean camera lens
3. **Express emotions clearly**: Exaggerated expressions work better
4. **Re-train model** (advanced): See training section below

### Issue 9: "Module not found" errors

**Problem**: `ModuleNotFoundError: No module named 'flask'` (or other modules)

**Solutions**:
1. **Activate virtual environment**:
   ```bash
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
   ```

2. **Reinstall dependencies**:
   ```bash
   pip install -r web_requirements.txt
   ```

3. **Verify installation**:
   ```bash
   pip list | grep flask  # macOS/Linux
   pip list | findstr flask  # Windows
   ```

---

## 📊 Training Your Own Model (Advanced)

If you want to train the model from scratch or fine-tune with your own data:

### Prerequisites
```bash
# Install training dependencies
pip install -r requirements.txt
```

### Step 1: Prepare Dataset

Download FER2013 dataset:
1. Go to [Kaggle FER2013](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data)
2. Download `fer2013.csv`
3. Place in project root directory

### Step 2: Preprocess Data

```bash
python utilities/preprocess_data.py
```

**What it does**:
- Loads raw FER2013 CSV data
- Splits into train/validation/test sets
- Applies data augmentation
- Saves preprocessed images

**Expected Output**:
```
Processed 28,709 training images
Processed 3,589 validation images
Processed 3,589 test images
```

### Step 3: Train Model

```bash
python utilities/train_model.py
```

**Training Parameters** (configurable in script):
- **Model**: Swin Transformer Base
- **Batch Size**: 32 (reduce to 16 if out of memory)
- **Epochs**: 50
- **Learning Rate**: 0.0001
- **Optimizer**: AdamW
- **Data Augmentation**: Rotation, flip, brightness, contrast

**Training Time**:
- CPU: ~24-48 hours
- GPU (GTX 1060): ~4-6 hours
- GPU (RTX 3070): ~2-3 hours

**Expected Output**:
```
Epoch 1/50
Train Loss: 1.8234, Train Acc: 25.43%
Val Loss: 1.6123, Val Acc: 32.18%

Epoch 2/50
Train Loss: 1.5678, Train Acc: 38.92%
Val Loss: 1.4567, Val Acc: 42.76%

...

Epoch 50/50
Train Loss: 0.4123, Train Acc: 85.67%
Val Loss: 0.5234, Val Acc: 78.92%

✅ Best model saved to: Models/Swin_Transformer/best_model.pth
```

### Step 4: Evaluate Model

```bash
python utilities/evaluate_model.py
```

**Outputs**:
- Classification report
- Confusion matrix
- Per-class accuracy
- Overall test accuracy

### Step 5: Upload to Hugging Face (Optional)

```bash
python upload_model.py
```

Follow prompts to upload your trained model to Hugging Face for sharing.

---

## 📁 Project Structure Explained

```
Facial-Expression-Recognition-FER-for-Mental-Health-Detection-/
│
├── 📄 web_app.py                    # Main Flask web application
│   └── Entry point for running the web interface
│
├── 📄 download_model.py             # Script to download pre-trained model
│   └── Downloads model from Hugging Face Hub
│
├── 📄 upload_model.py               # Script to upload model to Hugging Face
│   └── For sharing trained models
│
├── 📄 requirements.txt              # Training dependencies
│   └── Packages needed for model training
│
├── 📄 web_requirements.txt          # Web app dependencies
│   └── Packages needed to run web application (lighter)
│
├── 📄 README.md                     # Main project documentation
├── 📄 README2.md                    # This detailed setup guide
├── 📄 LICENSE                       # MIT License
├── 📄 FORK_SETUP_GUIDE.md          # Guide for forking the repository
│
├── 📁 Models/                       # Trained model files
│   └── 📁 Swin_Transformer/
│       ├── best_model.pth           # Pre-trained model weights (~400MB)
│       └── link_download_model.txt  # Hugging Face link
│
├── 📁 templates/                    # HTML templates for web app
│   └── 📄 index.html                # Main web interface
│       └── Neumorphic design with real-time emotion detection
│
├── 📁 utilities/                    # Training and evaluation scripts
│   ├── 📄 preprocess_data.py        # Data preprocessing and augmentation
│   ├── 📄 train_model.py            # Model training script
│   └── 📄 evaluate_model.py         # Model evaluation and metrics
│
├── 📁 images/                       # Documentation images
│   ├── facial-expression-recognition-augmented-dataset.jpg
│   ├── facial-expression-recognition-swin-transformer-model-architecture.jpg
│   ├── facial-emotion-recognition-grad-cam-visualizations.jpg
│   └── scopus-fer.jpg
│
└── 📁 .venv/                        # Virtual environment (created by you)
    └── Contains all installed Python packages
```

### Key Files Description

| File | Purpose | When to Use |
|------|---------|-------------|
| `web_app.py` | Main application | Run this to start the web interface |
| `download_model.py` | Model downloader | Run once to get the pre-trained model |
| `web_requirements.txt` | Web dependencies | Install these to run the web app |
| `requirements.txt` | Training dependencies | Install these to train models |
| `utilities/train_model.py` | Training script | Use to train from scratch |
| `utilities/evaluate_model.py` | Evaluation script | Test model performance |
| `templates/index.html` | Web interface | Frontend UI (HTML/CSS/JS) |

---

## ❓ FAQ (Frequently Asked Questions)

### General Questions

**Q1: Do I need a GPU to run this project?**

**A:** No. The web application runs fine on CPU. Training models is much faster with GPU, but not required.

---

**Q2: How accurate is the emotion detection?**

**A:** The model achieves ~78-80% accuracy on the FER2013 test set. Real-world accuracy depends on lighting, camera quality, and facial expression clarity.

---

**Q3: Can I use this for commercial purposes?**

**A:** Yes, this project is licensed under MIT License. You can use, modify, and distribute it freely. See LICENSE file for details.

---

**Q4: Does this work offline?**

**A:** Once you download the model, yes! The web application runs locally without internet connection. Internet is only needed for:
- Initial setup (downloading dependencies and model)
- Updating packages

---

**Q5: Can I detect multiple faces at once?**

**A:** Yes, the current version supports multiple face detection. Each detected face will get its own emotion analysis and depression risk score.

---

**Q6: How is depression risk calculated?**

**A:** The system analyzes emotion patterns:
- **Negative emotions** (sad, fear, angry) increase risk
- **Positive emotions** (happy) decrease risk
- **Note**: This is NOT a medical diagnosis, just an indicator for awareness

---

**Q7: Can I add more emotions?**

**A:** Yes, but you'll need to:
1. Modify the model architecture to support more classes
2. Retrain with a dataset that includes the new emotions
3. Update the web interface to display new emotions

---

### Technical Questions

**Q8: What's the difference between `requirements.txt` and `web_requirements.txt`?**

**A:** 
- `web_requirements.txt`: Minimal packages to run the web app (Flask, PyTorch, OpenCV)
- `requirements.txt`: Full packages including training tools (matplotlib, seaborn, albumentations)

For just using the web app, install `web_requirements.txt`.

---

**Q9: Why is the model file not in GitHub?**

**A:** GitHub has a 100MB file size limit. The model file (~400MB) is too large. We use Hugging Face for model hosting, which is designed for large ML models.

---

**Q10: Can I use a different model architecture?**

**A:** Yes! The code is modular. You can:
1. Modify `CustomSwinTransformer` class in `web_app.py`
2. Use models from `timm` library (ResNet, EfficientNet, ViT, etc.)
3. Train with `utilities/train_model.py`

---

**Q11: How do I update the project?**

**A:**
```bash
# Activate virtual environment
.venv\Scripts\activate

# Pull latest changes
git pull origin main

# Update dependencies
pip install -r web_requirements.txt --upgrade
```

---

**Q12: Can I deploy this to a web server?**

**A:** Yes! For production deployment:
1. Use a production WSGI server (Gunicorn, uWSGI)
2. Deploy to cloud platforms (Heroku, AWS, Google Cloud, Azure)
3. Ensure adequate CPU/GPU resources
4. Configure proper security (HTTPS, authentication)

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 web_app:app
```

---

**Q13: Why does the model load twice on startup?**

**A:** Flask's debug mode runs the application twice:
- Once for the main process
- Once for the reloader process

This is normal. To disable, set `debug=False` in `web_app.py`:
```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

---

**Q14: How do I change the port number?**

**A:** Edit `web_app.py`, change the last line:
```python
app.run(debug=True, host='0.0.0.0', port=8080)  # Change 5000 to 8080
```

---

**Q15: Can I use this with pre-recorded videos?**

**A:** The current version is designed for real-time webcam. To use videos:
1. Modify `web_app.py` to accept video file input
2. Use OpenCV's `cv2.VideoCapture('path/to/video.mp4')`
3. Process frames sequentially

---

### Data and Privacy Questions

**Q16: Is my webcam data stored or transmitted?**

**A:** No. All processing happens locally on your machine. Webcam data:
- Never leaves your computer
- Not stored to disk
- Not transmitted to any server
- Processed in memory in real-time only

---

**Q17: Can I use my own dataset?**

**A:** Yes! To train with custom data:
1. Organize images in folders by emotion:
   ```
   custom_dataset/
   ├── angry/
   ├── happy/
   ├── sad/
   └── ...
   ```
2. Modify `utilities/preprocess_data.py` to load your data
3. Run training: `python utilities/train_model.py`

---

**Q18: What dataset was used for training?**

**A:** FER2013 dataset:
- 35,887 grayscale images (48×48 pixels)
- 7 emotion categories
- Publicly available on Kaggle
- Used in academic research worldwide

---

### Performance Questions

**Q19: Why is the application slow on my computer?**

**A:** Common causes:
- **CPU-bound**: Model runs on CPU (normal, but slower)
- **Low RAM**: Close other applications
- **Old hardware**: Consider upgrading or reducing frame rate
- **High resolution webcam**: System processes large frames

Solutions:
- Reduce webcam resolution in system settings
- Close resource-heavy applications
- Use GPU acceleration if available

---

**Q20: How can I make it faster?**

**A:** Several options:
1. **Use GPU**:
   ```bash
   pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
   ```

2. **Reduce frame processing rate**: Modify `web_app.py` to process every other frame

3. **Use lighter model**: Replace Swin Transformer with MobileNet or EfficientNet

4. **Optimize image size**: Reduce input resolution in preprocessing

---

## 📞 Getting Help

If you encounter issues not covered in this guide:

1. **Check existing GitHub Issues**: [GitHub Issues](https://github.com/SEARO1/Facial-Expression-Recognition-FER-for-Mental-Health-Detection-/issues)

2. **Create a new issue**:
   - Click "New Issue"
   - Describe your problem with:
     - Operating System
     - Python version
     - Error messages (copy full text)
     - Steps you've tried

3. **Contact the author**:
   - Email: mujiyanto@amikom.ac.id
   - Include "FER Project Help" in subject line

4. **Community support**:
   - Stack Overflow (tag: `facial-recognition`, `pytorch`, `flask`)
   - Reddit: r/MachineLearning, r/learnmachinelearning

---

## 🎓 Learning Resources

Want to learn more about the technologies used?

### Computer Vision:
- [OpenCV Tutorial](https://docs.opencv.org/4.x/d9/df8/tutorial_root.html)
- [PyTorch Vision Tutorial](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)

### Deep Learning:
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [Fast.ai Course](https://course.fast.ai/)
- [Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning)

### Web Development:
- [Flask Documentation](https://flask.palletsprojects.com/)
- [HTML/CSS/JavaScript](https://www.w3schools.com/)

### Transformers:
- [Vision Transformer Paper](https://arxiv.org/abs/2010.11929)
- [Swin Transformer Paper](https://arxiv.org/abs/2103.14030)

---

## 🌟 Next Steps After Setup

Once you have the application running:

1. **Experiment with different expressions**: Test all 7 emotions
2. **Test lighting conditions**: See how it affects accuracy
3. **Try different distances**: Find optimal camera distance
4. **Multiple people**: Test with friends/family
5. **Read the research paper**: Understand the methodology
6. **Customize the UI**: Modify `templates/index.html`
7. **Train custom model**: Use your own facial expression data
8. **Deploy online**: Share with others via web hosting

---

## 📝 Change Log

### Version 1.0 (Current)
- Initial release with Swin Transformer model
- Real-time web application with Flask
- Depression risk analysis
- Support for 7 emotion classes
- Neumorphic UI design
- Hugging Face model hosting

### Planned Features (Future)
- [ ] Video file upload support
- [ ] Multiple face tracking
- [ ] Export emotion reports (PDF/CSV)
- [ ] Historical emotion tracking
- [ ] Mobile application
- [ ] REST API for integration
- [ ] Docker containerization
- [ ] Cloud deployment templates

---

## 🙏 Acknowledgments

This project uses:
- **FER2013 Dataset**: For training and evaluation
- **PyTorch**: Deep learning framework
- **Timm Library**: Pre-trained models
- **Flask**: Web framework
- **OpenCV**: Computer vision
- **Hugging Face**: Model hosting

Special thanks to:
- Research team at Universitas Amikom Yogyakarta
- Open-source community
- All contributors and testers

---

## 📄 License

This project is licensed under the MIT License.

**You are free to**:
- ✅ Use commercially
- ✅ Modify and adapt
- ✅ Distribute
- ✅ Use privately

**Requirements**:
- Include original license and copyright notice
- State changes made to the code

See [LICENSE](LICENSE) file for full details.

---

## 📚 Citation

If you use this project in your research or application, please cite:

```bibtex
@article{mujiyanto2024fer,
  title={Swin Transformer with Enhanced Dropout and Layer-wise Unfreezing for Facial Expression Recognition in Mental Health Detection},
  author={Mujiyanto, M. and Setyanto, A. and Kusrini, K. and Utami, E.},
  journal={Engineering, Technology \& Applied Science Research},
  volume={14},
  number={6},
  pages={19016--19023},
  year={2024},
  doi={10.48084/etasr.9139}
}
```

---

## 🎉 Conclusion

You now have everything you need to:
- ✅ Set up the project from scratch
- ✅ Run the web application
- ✅ Understand how it works
- ✅ Troubleshoot common issues
- ✅ Train custom models
- ✅ Extend the functionality

**Happy coding! 🚀**

If this guide helped you, please ⭐ star the repository on GitHub!

---

**Last Updated**: October 29, 2025

**Maintained by**: Mujiyanto (mujiyanto@amikom.ac.id)

**Repository**: [GitHub - SEARO1/Facial-Expression-Recognition-FER-for-Mental-Health-Detection-](https://github.com/SEARO1/Facial-Expression-Recognition-FER-for-Mental-Health-Detection-)

---

**Need more help?** Check out:
- 📖 [Main README.md](README.md)
- 🔧 [Setup Guide](SETUP_GUIDE.md)
- 🌐 [Web App Documentation](WEB_APP_README.md)
- 📧 [Contact Us](mailto:mujiyanto@amikom.ac.id)

