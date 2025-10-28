# 🍴 Fork Setup Guide - Option 1

This guide will help you fork the original repository and add your web application modifications.

---

## 📋 Overview

You'll be creating a **fork** of the original repository, which:

- ✅ Gives proper credit to the original author
- ✅ Maintains connection to the original project
- ✅ Shows it's a derivative work
- ✅ Allows you to pull updates from the original if needed

---

## 🚀 Step-by-Step Instructions

### Step 1: Fork the Original Repository on GitHub

1. **Go to the original repository:**

   - URL: https://github.com/mujiyantosvc/Facial-Expression-Recognition-FER-for-Mental-Health-Detection-

2. **Click the "Fork" button** (top-right corner of the page)

3. **Choose your account** as the destination

4. **Wait for GitHub to create your fork**
   - Your fork URL will be: `https://github.com/YOUR_USERNAME/Facial-Expression-Recognition-FER-for-Mental-Health-Detection-`

### Step 2: Clone Your Fork to a New Location

Open a terminal and run:

```bash
# Navigate to your Desktop or preferred location
cd c:\Users\cheun\Desktop

# Create a new folder for your fork
mkdir FER-WebApp-Fork
cd FER-WebApp-Fork

# Clone YOUR fork (replace YOUR_USERNAME with your GitHub username)
git clone https://github.com/YOUR_USERNAME/Facial-Expression-Recognition-FER-for-Mental-Health-Detection-.git
cd Facial-Expression-Recognition-FER-for-Mental-Health-Detection-
```

### Step 3: Copy Your Modified Files

Now copy the files I created for you from the original cloned folder to your fork:

**Option A: Use the automated script (Recommended)**

```bash
# Run the copy script from your ORIGINAL folder
cd c:\Users\cheun\Desktop\Face_Detect\Facial-Expression-Recognition-FER-for-Mental-Health-Detection-
python copy_to_fork.py
```

**Option B: Manual copy**

Copy these files from your original folder to your fork:

**New Files (created for web app):**

- `web_app.py`
- `templates/index.html`
- `download_model.py`
- `upload_model.py`
- `web_requirements.txt`
- `SETUP_GUIDE.md`
- `WEB_APP_README.md`
- `GITHUB_UPLOAD_GUIDE.md`
- `FORK_SETUP_GUIDE.md`
- Updated `.gitignore`
- Updated `README.md`

### Step 4: Update README to Show Your Modifications

In your fork's `README.md`, add a section at the top:

```markdown
# 🌟 Enhanced with Web Application

This is a fork of the original [Facial Expression Recognition project](https://github.com/mujiyantosvc/Facial-Expression-Recognition-FER-for-Mental-Health-Detection-) by mujiyantosvc.

## 🆕 What's New in This Fork

- ✅ **Real-time Web Application**: Live facial emotion detection via webcam
- ✅ **Neumorphism UI**: Beautiful soft UI design (black, white, brown colors)
- ✅ **Depression Risk Analysis**: Mental health assessment based on emotional patterns
- ✅ **Easy Setup**: Simplified installation with Hugging Face integration
- ✅ **Team Collaboration**: Ready for group projects with comprehensive documentation

See [WEB_APP_README.md](./WEB_APP_README.md) for web application documentation.

---

# Original README Below

[Keep the rest of the original README content here]
```

### Step 5: Commit Your Changes

```bash
# Make sure you're in your fork directory
cd c:\Users\cheun\Desktop\FER-WebApp-Fork\Facial-Expression-Recognition-FER-for-Mental-Health-Detection-

# Check what files will be committed
git status

# Add all new and modified files
git add .

# Commit with a descriptive message
git commit -m "Add web application with neumorphism UI and depression detection"

# Push to your fork
git push origin main
```

### Step 6: Upload Model to Hugging Face

```bash
# Upload your trained model
python upload_model.py
```

Follow the prompts to upload to Hugging Face.

### Step 7: Update Documentation URLs

After uploading to Hugging Face, update these files with your actual URLs:

**In `README.md`:**

- Replace `YOUR_USERNAME/YOUR_REPO_NAME` with your GitHub username and repo name
- Replace `YOUR_USERNAME/MODEL_REPO_NAME` with your Hugging Face repo

**In `SETUP_GUIDE.md`:**

- Same replacements as above

**In `WEB_APP_README.md`:**

- Same replacements as above

Then commit and push again:

```bash
git add README.md SETUP_GUIDE.md WEB_APP_README.md
git commit -m "Update documentation with actual repository URLs"
git push origin main
```

---

## 🎯 What Your Fork Will Contain

### Files from Original Repository:

- ✅ Training scripts (`utilities/`)
- ✅ Original prediction scripts
- ✅ Dataset processing scripts
- ✅ Images and visualizations
- ✅ Original documentation
- ✅ License

### Your New Additions:

- ✅ Web application (`web_app.py`)
- ✅ Web UI template (`templates/index.html`)
- ✅ Model download/upload scripts
- ✅ Web app documentation
- ✅ Setup guides
- ✅ Updated README

### Excluded (via .gitignore):

- ❌ Model files (hosted on Hugging Face)
- ❌ Dataset files (too large)
- ❌ Virtual environment
- ❌ Cache files

---

## 👥 Sharing with Your Team

Once your fork is set up, share this with your team:

1. **Your GitHub Fork URL:**

   ```
   https://github.com/YOUR_USERNAME/Facial-Expression-Recognition-FER-for-Mental-Health-Detection-
   ```

2. **Your Hugging Face Model URL:**

   ```
   https://huggingface.co/YOUR_USERNAME/MODEL_REPO_NAME
   ```

3. **Quick Start for Team Members:**

   ```bash
   # Clone your fork
   git clone https://github.com/YOUR_USERNAME/Facial-Expression-Recognition-FER-for-Mental-Health-Detection-.git
   cd Facial-Expression-Recognition-FER-for-Mental-Health-Detection-

   # Setup environment
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r web_requirements.txt

   # Download model
   python download_model.py

   # Run web app
   python web_app.py
   ```

---

## 🔄 Keeping Your Fork Updated

If the original repository gets updates, you can sync them:

```bash
# Add the original repository as upstream
git remote add upstream https://github.com/mujiyantosvc/Facial-Expression-Recognition-FER-for-Mental-Health-Detection-.git

# Fetch updates from original
git fetch upstream

# Merge updates into your fork
git merge upstream/main

# Push to your fork
git push origin main
```

---

## ✅ Verification Checklist

Before sharing with your team:

- [ ] Forked the original repository on GitHub
- [ ] Cloned your fork to a new location
- [ ] Copied all modified files to your fork
- [ ] Updated README with fork information
- [ ] Committed and pushed changes
- [ ] Uploaded model to Hugging Face
- [ ] Updated documentation with actual URLs
- [ ] Tested that team members can clone and run
- [ ] Verified .gitignore excludes large files

---

## 🆘 Troubleshooting

### Issue: "Permission denied" when pushing

**Solution:** Make sure you're pushing to YOUR fork, not the original repository.

```bash
# Check your remote URL
git remote -v

# Should show YOUR username, not mujiyantosvc
# If wrong, update it:
git remote set-url origin https://github.com/YOUR_USERNAME/Facial-Expression-Recognition-FER-for-Mental-Health-Detection-.git
```

### Issue: Large files rejected by GitHub

**Solution:** Make sure `.gitignore` is properly set up and committed first:

```bash
git add .gitignore
git commit -m "Add gitignore"
git push
```

Then remove any large files from git history if needed.

---

## 📧 Questions?

See [SETUP_GUIDE.md](./SETUP_GUIDE.md) for detailed setup instructions or [GITHUB_UPLOAD_GUIDE.md](./GITHUB_UPLOAD_GUIDE.md) for upload guidelines.

---

**Good luck with your fork! 🎉**
