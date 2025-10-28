# 📤 GitHub Upload Guide

This guide explains what files to upload to GitHub and how to integrate with Hugging Face for your team collaboration.

---

## 📦 Part 1: Files to Upload to GitHub

### ✅ Files to INCLUDE in GitHub

Upload these files to your GitHub repository:

#### **Core Application Files**

- `web_app.py` - Flask web application
- `predict_single_image.py` - Single image prediction
- `predict_webcam.py` - Webcam prediction (standalone)
- `download_model.py` - Download model from Hugging Face
- `upload_model.py` - Upload model to Hugging Face

#### **Utility Scripts**

- `utilities/train_model.py` - Model training script
- `utilities/evaluate_model.py` - Model evaluation
- `utilities/preprocess_data.py` - Data preprocessing

#### **Web Interface**

- `templates/index.html` - Web UI template

#### **Configuration Files**

- `requirements.txt` - Training dependencies
- `web_requirements.txt` - Web app dependencies
- `.gitignore` - Git ignore rules
- `.gitattributes` - Git attributes

#### **Documentation**

- `README.md` - Main project documentation
- `SETUP_GUIDE.md` - Team setup instructions
- `WEB_APP_README.md` - Web app documentation
- `HOW_TO_USE_MODEL.md` - Model usage guide
- `POST_TRAINING_GUIDE.md` - Post-training guide
- `usage_guide.md` - General usage guide
- `GITHUB_UPLOAD_GUIDE.md` - This file
- `LICENSE` - Project license

#### **Images/Assets**

- `images/` - All visualization images

---

### ❌ Files to EXCLUDE from GitHub

**DO NOT upload these files** (they're already in `.gitignore`):

#### **Model Files** (Too large - use Hugging Face instead)

- `Models/` folder
- `*.pth` files
- `*.pt` files
- `*.ckpt` files

#### **Dataset Files** (Too large)

- `datasets/` folder
- `FER2013_processed/` folder
- `fer2013/` folder
- `*.csv` files (dataset CSVs)
- `*.zip` files
- `*.tar.gz` files

#### **Environment & Cache**

- `.venv/` - Virtual environment
- `__pycache__/` - Python cache
- `.cache/` - Cache files
- `*.pyc` - Compiled Python

#### **Temporary Files**

- `README_HF.md` - Generated during upload
- `config.json` - Generated during upload

---

## 🤗 Part 2: Model Files on Hugging Face

### What Goes on Hugging Face

Upload these to your Hugging Face repository:

1. **best_model.pth** - Trained model weights (~400MB)
2. **README.md** - Model documentation (auto-generated)
3. **config.json** - Model configuration (auto-generated)

### How to Upload to Hugging Face

```bash
python upload_model.py
```

Follow the prompts:

1. Enter your Hugging Face token
2. Enter your username
3. Enter repository name (or use default)

The script will automatically:

- Create the repository
- Generate documentation
- Upload the model
- Provide you with the model URL

---

## 🔄 Integration: How GitHub + Hugging Face Work Together

### The Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                     YOUR PROJECT                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────┐              ┌──────────────────┐    │
│  │   GitHub Repo    │              │  Hugging Face    │    │
│  │                  │              │                  │    │
│  │  • Code          │              │  • Model (.pth)  │    │
│  │  • Scripts       │              │  • README        │    │
│  │  • Templates     │              │  • Config        │    │
│  │  • Docs          │              │                  │    │
│  └──────────────────┘              └──────────────────┘    │
│           │                                 │               │
│           │                                 │               │
│           ▼                                 ▼               │
│  ┌─────────────────────────────────────────────────┐       │
│  │         Your Groupmate's Computer                │       │
│  │                                                  │       │
│  │  1. git clone (from GitHub)                     │       │
│  │  2. python download_model.py (from Hugging Face)│       │
│  │  3. python web_app.py (run application)         │       │
│  └─────────────────────────────────────────────────┘       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 📝 Step-by-Step: Preparing for GitHub Upload

### Step 1: Upload Model to Hugging Face First

```bash
# Make sure you're in the project directory
cd Facial-Expression-Recognition-FER-for-Mental-Health-Detection-

# Upload the model
python upload_model.py
```

**Important**: Note down your Hugging Face repository URL!
Example: `https://huggingface.co/YOUR_USERNAME/facial-expression-recognition-mental-health`

### Step 2: Update Documentation with Your URLs

Edit these files and replace placeholders:

**In `README.md`:**

- Replace `YOUR_USERNAME/YOUR_REPO_NAME` with your GitHub repo
- Replace `YOUR_USERNAME/MODEL_REPO_NAME` with your Hugging Face repo

**In `SETUP_GUIDE.md`:**

- Replace `YOUR_USERNAME/YOUR_REPO_NAME` with your GitHub repo
- Replace `YOUR_USERNAME/facial-expression-recognition-mental-health` with your Hugging Face repo

### Step 3: Verify .gitignore

Make sure `.gitignore` is properly configured:

```bash
# Check what will be committed
git status

# You should NOT see:
# - Models/ folder
# - datasets/ folder
# - FER2013_processed/ folder
# - .venv/ folder
# - __pycache__/ folders
```

### Step 4: Commit and Push to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files (respecting .gitignore)
git add .

# Commit
git commit -m "Initial commit: Facial Expression Recognition project"

# Add remote (replace with your GitHub repo URL)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git push -u origin main
```

---

## 👥 For Your Groupmates: How to Get Started

Share this with your team members:

### Quick Start Instructions

1. **Clone the GitHub repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```

2. **Set up Python environment**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   pip install -r web_requirements.txt
   ```

3. **Download the model from Hugging Face**

   ```bash
   python download_model.py
   ```

   When prompted, enter: `YOUR_USERNAME/MODEL_REPO_NAME`

4. **Run the application**

   ```bash
   python web_app.py
   ```

5. **Open browser**
   Go to: `http://localhost:5000`

**Full instructions**: See [SETUP_GUIDE.md](./SETUP_GUIDE.md)

---

## 🔍 Verification Checklist

Before sharing with your team, verify:

- [ ] Model uploaded to Hugging Face successfully
- [ ] GitHub repository created
- [ ] All code files committed to GitHub
- [ ] Large files (models, datasets) NOT in GitHub
- [ ] `.gitignore` properly configured
- [ ] README.md updated with correct URLs
- [ ] SETUP_GUIDE.md updated with correct URLs
- [ ] Tested the download_model.py script
- [ ] Verified groupmates can clone and run

---

## 📊 File Size Reference

### GitHub (Small files only)

- Total size: ~5-10 MB
- Includes: Code, templates, docs, images

### Hugging Face (Large files)

- Model file: ~400 MB
- Total size: ~400 MB

### Not Uploaded Anywhere (Local only)

- Datasets: ~300 MB
- Processed data: ~500 MB
- Virtual environment: ~500 MB

---

## 🆘 Troubleshooting

### Issue: "File too large" error on GitHub

**Solution**: The file is probably in `.gitignore` but was committed before. Remove it:

```bash
git rm --cached path/to/large/file
git commit -m "Remove large file"
git push
```

### Issue: Groupmate can't download model

**Solution**:

1. Verify Hugging Face repository is public
2. Check the repository ID is correct
3. Try manual download from Hugging Face website

### Issue: Git shows too many files

**Solution**: Make sure `.gitignore` is committed:

```bash
git add .gitignore
git commit -m "Add gitignore"
```

---

## 💡 Best Practices

1. **Always upload model to Hugging Face BEFORE pushing to GitHub**
2. **Test the download_model.py script before sharing**
3. **Keep documentation URLs updated**
4. **Use meaningful commit messages**
5. **Don't commit sensitive information** (API keys, tokens)
6. **Regularly pull updates** from GitHub
7. **Communicate changes** with your team

---

## 📞 Support

If your groupmates have issues:

1. Direct them to [SETUP_GUIDE.md](./SETUP_GUIDE.md)
2. Check the Troubleshooting section
3. Verify their Python version (3.8+)
4. Ensure they have internet connection for downloads

---

## ✅ Summary

**GitHub Contains:**

- ✅ All code and scripts
- ✅ Documentation
- ✅ Templates and UI
- ✅ Configuration files

**Hugging Face Contains:**

- ✅ Trained model (best_model.pth)
- ✅ Model documentation

**Your Groupmates Need:**

1. Clone from GitHub
2. Download model from Hugging Face (using download_model.py)
3. Run the application

**That's it!** 🎉

---

**Questions?** Check [SETUP_GUIDE.md](./SETUP_GUIDE.md) or contact the project maintainer.
