# Facial Expression Recognition (FER) for Mental Health Detection Using Transformer Model

![Python 3.10](https://img.shields.io/badge/python-3.10-green.svg?style=plastic)
![PyTorch 2.0](https://img.shields.io/badge/pytorch-2.0-green.svg?style=plastic)
![CUDA 11](https://img.shields.io/badge/cuda-11-green.svg?style=plastic)
![License CC BY 4.0](https://img.shields.io/badge/license-MIT-green.svg?style=plastic)

Welcome to the **Facial Expression Recognition (FER) for Mental Health Detection** repository. This project leverages cutting-edge AI models, including **Swin Transformer**, to analyze facial expressions for detecting mental health conditions. For detailed insights, refer to the [research paper published in Engineering, Technology & Applied Science Research](https://doi.org/10.48084/etasr.9139), indexed in Scopus Q2.

---

## 🚀 Quick Start for Team Members

**New to this project?** Follow our comprehensive setup guide:

👉 **[SETUP_GUIDE.md](./SETUP_GUIDE.md)** - Complete instructions for getting started

### Quick Setup (5 Steps)

```bash
# 1. Clone the repository
git clone https://github.com/SEARO1/Facial-Expression-Recognition-FER-for-Mental-Health-Detection-
cd Facial-Expression-Recognition-FER-for-Mental-Health-Detection-

# 2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# 3. Install dependencies
pip install -r web_requirements.txt

# 4. Download the trained model from Hugging Face&&Enter repo id: SEARO1/FER_model
python download_model.py

# 5. Run the web application
python web_app.py
```

Open your browser at **http://localhost:5000** and start detecting emotions! 🎉

---

## 📦 Project Components

This repository is organized into **two main parts**:

### Part 1: Code Repository (GitHub)

All source code, scripts, and documentation are hosted here on GitHub:

- ✅ Web application (`web_app.py`)
- ✅ Training scripts (`utilities/`)
- ✅ Prediction scripts (`predict_*.py`)
- ✅ Documentation and guides
- ✅ UI templates

### Part 2: Trained Model (Hugging Face)

The trained model files are hosted on Hugging Face due to their large size:

- 🤗 **Model Repository**: `https://huggingface.co/YOUR_USERNAME/MODEL_REPO_NAME`
- 📥 **Download Script**: Use `python download_model.py` to automatically download
- 📊 **Model Size**: ~400MB

**Why separate?** Large model files (`.pth`) are not suitable for GitHub. We use Hugging Face for model hosting and GitHub for code, making it easy for team members to collaborate!

---

## 🌐 Web Application

This project includes a **real-time facial expression recognition web application** with:

- 📹 **Live Camera Detection**: Real-time emotion detection from your webcam
- 🎨 **Neumorphism UI**: Beautiful soft UI design (black, white, brown colors)
- 😊 **7 Emotion Classes**: Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise
- 🧠 **Depression Risk Analysis**: Mental health risk assessment based on emotional patterns
- ⚡ **Fast Performance**: Optimized for real-time processing

**Documentation**: See [WEB_APP_README.md](./WEB_APP_README.md) for detailed web app documentation.

---

## 📘 Overview of Facial Expression Recognition Techniques Using Python

Mental health issues such as **anxiety**, **depression**, **OCD (Obsessive Compulsive Disorder)**, **PTSD (Post-Traumatic Stress Disorder)**, and other conditions significantly impact individuals and society. Early detection and intervention can drastically improve outcomes, and **Facial Expression Recognition (FER)** provides a non-invasive and efficient way to monitor emotional states.

This repository combines **Artificial Intelligence for Mental Health** with advanced **Facial Emotion Recognition** techniques to identify subtle changes in expressions that indicate mental health risks. The project leverages cutting-edge models, including **Swin Transformers**, **Vision Transformers (ViT)**, and **Custom CNNs**, integrated with robust datasets such as **FER2013** and **CK+**. These models are designed to:

- Recognize emotions like happiness, sadness, anger, fear, and surprise.
- Detect early signs of mental health conditions such as **serious mental illness** and stress-related disorders.
- Provide practical applications in **AI Emotion Recognition** for healthcare, HR, and research.

**Key Features:**

- High-accuracy emotion detection using **deep learning for facial expression recognition**.
- Integration with **mental health scoring systems** to quantify emotional health.
- Applications in **real-time emotion detection systems** and **emotion detection using OpenCV Python**.

---

## 📂 Repository Structure

```
📦FER-for-Mental-Health-Detection
├── 📁 Models (Download from Hugging Face)
│   └── 📁 Swin_Transformer
│       └── best_model.pth (use download_model.py)
├── 📁 templates
│   └── index.html (Web UI)
├── 📁 utilities
│   ├── train_model.py
│   ├── evaluate_model.py
│   └── preprocess_data.py
├── 📁 images (Visualizations)
├── 📄 web_app.py (Flask web application)
├── 📄 download_model.py (Download model from Hugging Face)
├── 📄 upload_model.py (Upload model to Hugging Face)
├── 📄 predict_single_image.py
├── 📄 predict_webcam.py
├── 📄 SETUP_GUIDE.md (Team setup instructions)
├── 📄 WEB_APP_README.md (Web app documentation)
├── 📄 README.md (This file)
├── 📄 requirements.txt (Training dependencies)
└── 📄 web_requirements.txt (Web app dependencies)
```

---

## 📚 Datasets

### FER2013

- **Description**: A dataset of 35,887 grayscale images labeled with seven emotions (Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral).
- **Source**: [FER2013 on Kaggle](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge).

---

## 💡 Models and Architectures

### 1. Swin Transformer

- **Description**: A hierarchical transformer optimized for visual tasks, ideal for **facial expression recognition** and mental health detection.
- **Reference**: [Swin Transformer Paper](https://arxiv.org/abs/2103.14030)

### 2. Custom CNN

- **Description**: Lightweight CNN for real-time emotion detection, suitable for **AI Emotion Recognition** tasks.

### 3. Vision Transformer (ViT)

- **Description**: Captures long-range dependencies in facial features for robust **facial emotion recognition**.
- **Reference**: [ViT Paper](https://arxiv.org/abs/2010.11929)

### 4. Additional Models

- Includes MobileNet, EfficientNet, and hybrid architectures for **real-time emotion detection**.

---

## 📷 Visualizations

### Augmented Images

![Augmented Images](./images/facial-expression-recognition-augmented-dataset.jpg)

- Visualizes data augmentation techniques used to enhance model robustness.

### Model Architecture

![FER Architecture](./images/facial-expression-recognition-swin-transformer-model-architecture.jpg)

- Diagram of the Swin Transformer model optimized for **facial expression recognition**.

### Grad-CAM Visualizations

![Grad-CAM Visualization](./images/facial-emotion-recognition-grad-cam-visualizations.jpg)

- Highlights the facial regions influencing the model's predictions.

### Mental Health Scoring Summary

| **Employee ID** | **Avg Confidence** | **No. of Images** | **Mental Health Score** |
| --------------- | ------------------ | ----------------- | ----------------------- |
| 31              | 0.7747             | 30                | 52.03                   |
| 39              | 0.9230             | 30                | 53.00                   |
| 16              | 0.8943             | 30                | 53.00                   |
| 15              | 0.6484             | 30                | 50.93                   |
| 17              | 0.7503             | 30                | 51.07                   |

---

## 📈 Applications

- **Human Resources**: Monitor and assess employee mental health using **AI for mental health detection**.
- **Healthcare**: Real-time emotion detection for early mental health interventions.
- **Research**: Advance the field of **artificial intelligence in mental health detection**.
- **Education**: Mental health monitoring for students.
- **Customer Service**: Emotion-aware customer interaction systems.

---

## 🔗 Important Links

- **GitHub Repository**: This repository
- **Hugging Face Model**: `https://huggingface.co/YOUR_USERNAME/MODEL_REPO_NAME`
- **Setup Guide**: [SETUP_GUIDE.md](./SETUP_GUIDE.md)
- **Web App Documentation**: [WEB_APP_README.md](./WEB_APP_README.md)
- **Research Paper**: [DOI: 10.48084/etasr.9139](https://doi.org/10.48084/etasr.9139)

---

## 📄 Citation

This research has been published in **Engineering, Technology & Applied Science Research**, indexed in **Scopus Q2**. Below is the certification evidence:

<img src="./images/scopus-fer.jpg" alt="Scopus Q2 Certification" width="200">

### Citation Formats

**APA:**

> Mujiyanto, M., Setyanto, A., Kusrini, K., & Utami, E. (2024). Swin Transformer with Enhanced Dropout and Layer-wise Unfreezing for Facial Expression Recognition in Mental Health Detection. Engineering, Technology & Applied Science Research, 14(6), 19016–19023. https://doi.org/10.48084/etasr.9139

**MLA:**

> Mujiyanto, M., et al. "Facial Expression Recognition (FER) for Mental Health Detection." Engineering, Technology & Applied Science Research, vol. 14, no. 6, 2024, pp. 19016-19023.

**Vancouver:**

> Mujiyanto M, et al. Facial Expression Recognition (FER) for Mental Health Detection. Engineering, Technology & Applied Science Research. 2024;14(6):19016-23.

---

## 📧 Contact

For questions or support, please contact:

- **Email**: [mujiyanto@amikom.ac.id](mailto:mujiyanto@amikom.ac.id)

### Special Credit

- **Description**: Indonesia artificial intelligence AI Developer | Website Developer | Mobile Developer | Software Developer | Software House Indonesia
- **Reference**: [Second Vision Corp](https://secondvisioncorp.com/)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**⭐ If you find this project helpful, please star the repository!**
