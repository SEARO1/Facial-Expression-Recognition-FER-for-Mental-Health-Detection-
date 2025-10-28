# 🚀 Setup Guide for Team Members

This guide will help you set up the Facial Expression Recognition project on your local machine.

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Quick Start](#quick-start)
3. [Detailed Setup Instructions](#detailed-setup-instructions)
4. [Running the Web Application](#running-the-web-application)
5. [Training Your Own Model (Optional)](#training-your-own-model-optional)
6. [Troubleshooting](#troubleshooting)

---

## ✅ Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads/)
- **Webcam** (for real-time emotion detection)

---

## 🚀 Quick Start

Follow these steps to get the project running quickly:

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### Step 2: Create Virtual Environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r web_requirements.txt
```

### Step 4: Download the Trained Model

```bash
python download_model.py
```

When prompted, enter the Hugging Face repository ID:

```
YOUR_USERNAME/facial-expression-recognition-mental-health
```

### Step 5: Run the Web Application

```bash
python web_app.py
```

Open your browser and go to: **http://localhost:5000**

🎉 **That's it! You're ready to use the application!**

---

## 📖 Detailed Setup Instructions

### 1. Clone the Repository

Open your terminal/command prompt and run:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

This will download all the project files to your local machine.

### 2. Set Up Python Virtual Environment

A virtual environment keeps your project dependencies isolated.

**Windows:**

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate

# You should see (.venv) in your terminal prompt
```

**macOS/Linux:**

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# You should see (.venv) in your terminal prompt
```

### 3. Install Required Packages

The project has two requirement files:

- `web_requirements.txt` - For running the web application (recommended)
- `requirements.txt` - For training models (only if you want to train)

**For Web Application (Most Users):**

```bash
pip install -r web_requirements.txt
```

**For Model Training (Advanced Users):**

```bash
pip install -r requirements.txt
```

### 4. Download the Pre-trained Model

The trained model is hosted on Hugging Face (not in GitHub due to its large size).

**Option A: Interactive Download (Recommended)**

```bash
python download_model.py
```

Follow the prompts and enter the Hugging Face repository ID when asked.

**Option B: Manual Download**

1. Go to the Hugging Face repository: `https://huggingface.co/YOUR_USERNAME/REPO_NAME`
2. Download `best_model.pth`
3. Create folder structure: `Models/Swin_Transformer/`
4. Place the downloaded file in: `Models/Swin_Transformer/best_model.pth`

### 5. Verify Installation

Check that everything is set up correctly:

```bash
# Check Python version
python --version

# Check if model exists
# Windows:
dir Models\Swin_Transformer\best_model.pth

# macOS/Linux:
ls -lh Models/Swin_Transformer/best_model.pth
```

---

## 🌐 Running the Web Application

### Start the Application

```bash
python web_app.py
```

You should see:

```
Loading model...
Model loaded successfully!
============================================================
Starting Flask Web Application
Open your browser and go to: http://localhost:5000
============================================================
```

### Access the Application

1. Open your web browser
2. Go to: **http://localhost:5000**
3. Allow camera access when prompted
4. The application will start detecting your facial expressions!

### Features

- **Real-time Emotion Detection**: Detects 7 emotions (Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise)
- **Depression Risk Analysis**: Analyzes emotional patterns
- **Beautiful Neumorphism UI**: Soft, modern interface with black, white, and brown colors

### Stop the Application

Press `Ctrl + C` in the terminal to stop the server.

---

## 🎓 Training Your Own Model (Optional)

If you want to train the model from scratch:

### 1. Download the Dataset

Download the FER2013 dataset and place it in the `datasets/` folder.

### 2. Preprocess the Data

```bash
python utilities/preprocess_data.py
```

### 3. Train the Model

```bash
python utilities/train_model.py
```

Training will take several hours depending on your hardware.

### 4. Evaluate the Model

```bash
python utilities/evaluate_model.py
```

---

## 🔧 Troubleshooting

### Issue: "Module not found" error

**Solution:**

```bash
# Make sure virtual environment is activated
# Then reinstall dependencies
pip install -r web_requirements.txt
```

### Issue: Model download fails

**Solution:**

1. Check your internet connection
2. Verify the Hugging Face repository ID is correct
3. Make sure the repository is public
4. Try manual download from Hugging Face website

### Issue: Camera not working

**Solution:**

1. Check browser permissions (allow camera access)
2. Make sure no other application is using the camera
3. Try a different browser (Chrome recommended)
4. Check if camera works in other applications

### Issue: "Port 5000 already in use"

**Solution:**

```bash
# Windows: Find and kill the process
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F

# macOS/Linux: Find and kill the process
lsof -ti:5000 | xargs kill -9
```

Or change the port in `web_app.py`:

```python
app.run(debug=True, port=5001)  # Use port 5001 instead
```

### Issue: Low FPS or slow detection

**Solution:**

1. Close other applications to free up resources
2. Use a GPU if available (requires CUDA setup)
3. Reduce video quality in browser settings

### Issue: Virtual environment activation fails

**Windows PowerShell:**

```bash
# If you get execution policy error
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.venv\Scripts\activate
```

---

## 📁 Project Structure

```
Facial-Expression-Recognition/
├── web_app.py                 # Main Flask application
├── download_model.py          # Model download script
├── upload_model.py            # Upload model to Hugging Face
├── predict_single_image.py    # Predict single image
├── predict_webcam.py          # Webcam prediction (standalone)
├── requirements.txt           # Training dependencies
├── web_requirements.txt       # Web app dependencies
├── SETUP_GUIDE.md            # This file
├── README.md                 # Project overview
├── WEB_APP_README.md         # Web app documentation
├── templates/
│   └── index.html            # Web interface
├── utilities/
│   ├── train_model.py        # Model training script
│   ├── evaluate_model.py     # Model evaluation
│   └── preprocess_data.py    # Data preprocessing
└── Models/
    └── Swin_Transformer/
        └── best_model.pth    # Trained model (download required)
```

---

## 🔗 Important Links

- **GitHub Repository**: `https://github.com/YOUR_USERNAME/YOUR_REPO_NAME`
- **Hugging Face Model**: `https://huggingface.co/YOUR_USERNAME/MODEL_REPO_NAME`
- **Project Documentation**: See `README.md`
- **Web App Guide**: See `WEB_APP_README.md`

---

## 👥 Team Collaboration

### Updating Your Local Repository

```bash
# Get latest changes from GitHub
git pull origin main

# If you made local changes
git stash          # Save your changes
git pull           # Get updates
git stash pop      # Restore your changes
```

### Sharing Your Changes

```bash
# Check what files changed
git status

# Add your changes
git add .

# Commit with a message
git commit -m "Description of your changes"

# Push to GitHub
git push origin main
```

---

## 💡 Tips

1. **Always activate the virtual environment** before running any Python scripts
2. **Keep your dependencies updated**: `pip install --upgrade -r web_requirements.txt`
3. **Don't commit large files** (models, datasets) to GitHub - use Hugging Face instead
4. **Test on different browsers** if you encounter issues
5. **Check the terminal output** for error messages

---

## 📞 Getting Help

If you encounter issues:

1. Check this guide's [Troubleshooting](#troubleshooting) section
2. Read the error message carefully
3. Search for the error online
4. Ask your team members
5. Check the project's GitHub Issues page

---

## ✨ Next Steps

After setup, you can:

1. **Explore the web application** - Test different facial expressions
2. **Read the documentation** - Check `README.md` and `WEB_APP_README.md`
3. **Customize the UI** - Modify `templates/index.html`
4. **Improve the model** - Train with more data or different architectures
5. **Add new features** - Extend the application functionality

---

**Happy Coding! 🎉**

If you found this guide helpful, please star ⭐ the repository!
