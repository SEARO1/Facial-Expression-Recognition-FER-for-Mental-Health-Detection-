"""
Upload Facial Expression Recognition Model to Hugging Face
This script uploads the trained Swin Transformer model to Hugging Face Hub
"""

import os
import torch
import timm
from huggingface_hub import HfApi, login, create_repo
import json
from pathlib import Path

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

def create_model_card(repo_id, model_info):
    """Create a comprehensive model card"""
    model_card = f"""---
language: en
license: mit
tags:
- facial-expression-recognition
- emotion-detection
- mental-health
- swin-transformer
- pytorch
- computer-vision
datasets:
- FER2013
metrics:
- accuracy
- f1-score
library_name: pytorch
---

# Facial Expression Recognition for Mental Health Detection

## Model Description

This model is a **Swin Transformer** fine-tuned for facial expression recognition (FER) with applications in mental health detection. It can classify facial expressions into 7 categories and provide depression risk analysis based on emotional patterns.

### Model Architecture

- **Base Model**: Swin Transformer (swin_base_patch4_window7_224)
- **Custom Classifier**: 
  - Linear layer (backbone features → 512)
  - ReLU activation
  - Dropout (p=0.6)
  - Linear layer (512 → 7 classes)

### Emotion Classes

The model predicts 7 facial expressions:
1. **Angry** 😠
2. **Disgust** 🤢
3. **Fear** 😨
4. **Happy** 😊
5. **Neutral** 😐
6. **Sad** 😢
7. **Surprise** 😲

## Training Details

### Dataset

- **Name**: FER2013 (Facial Expression Recognition 2013)
- **Size**: ~35,000 grayscale images (48x48 pixels)
- **Split**: Train/Validation/Test

### Training Configuration

{model_info}

## Usage

### Installation

```bash
pip install torch torchvision timm huggingface_hub
```

### Load Model

```python
import torch
import timm
from huggingface_hub import hf_hub_download

class CustomSwinTransformer(torch.nn.Module):
    def __init__(self, pretrained=True, num_classes=7):
        super(CustomSwinTransformer, self).__init__()
        self.backbone = timm.create_model('swin_base_patch4_window7_224', 
                                         pretrained=pretrained, num_classes=0)
        self.classifier = torch.nn.Sequential(
            torch.nn.Linear(self.backbone.num_features, 512),
            torch.nn.ReLU(),
            torch.nn.Dropout(p=0.6),
            torch.nn.Linear(512, num_classes)
        )

    def forward(self, x):
        x = self.backbone(x)
        return self.classifier(x)

# Download and load model
model_path = hf_hub_download(repo_id="{repo_id}", filename="best_model.pth")
model = CustomSwinTransformer(pretrained=False, num_classes=7)
model.load_state_dict(torch.load(model_path, map_location='cpu'), strict=False)
model.eval()
```

### Inference Example

```python
from torchvision import transforms
from PIL import Image

# Prepare image
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

image = Image.open("face.jpg").convert("RGB")
input_tensor = transform(image).unsqueeze(0)

# Predict
with torch.no_grad():
    output = model(input_tensor)
    probabilities = torch.nn.functional.softmax(output, dim=1)
    predicted_class = torch.argmax(probabilities, dim=1)

emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
print(f"Predicted Emotion: {{emotions[predicted_class.item()]}}")
print(f"Confidence: {{probabilities[0][predicted_class].item()*100:.2f}}%")
```

## Mental Health Application

This model can be used for depression risk analysis by analyzing emotional patterns:

### Depression Risk Calculation

```python
def analyze_depression_risk(emotion_probs):
    sad_score = emotion_probs[5]  # Sad
    fear_score = emotion_probs[2]  # Fear
    angry_score = emotion_probs[0]  # Angry
    happy_score = emotion_probs[3]  # Happy
    
    negative_emotions = (sad_score * 0.4 + fear_score * 0.3 + angry_score * 0.3)
    positive_emotions = happy_score
    
    depression_risk = (negative_emotions * 100) - (positive_emotions * 20)
    depression_risk = max(0, min(100, depression_risk))
    
    if depression_risk < 30:
        return "Low Risk"
    elif depression_risk < 60:
        return "Moderate Risk"
    else:
        return "High Risk"
```

⚠️ **Important**: This is an educational tool and should NOT replace professional medical advice or diagnosis.

## Performance

The model achieves competitive performance on the FER2013 dataset. See the training logs for detailed metrics.

## Limitations

- Trained on FER2013 dataset which may not represent all demographics equally
- Performance may vary with different lighting conditions, angles, and image quality
- Should not be used as the sole basis for mental health diagnosis
- Requires frontal face images for best results

## Citation

If you use this model, please cite:

```bibtex
@misc{{fer-mental-health-2024,
  author = {{Your Name}},
  title = {{Facial Expression Recognition for Mental Health Detection}},
  year = {{2024}},
  publisher = {{Hugging Face}},
  howpublished = {{\\url{{https://huggingface.co/{repo_id}}}}}
}}
```

## License

MIT License - See LICENSE file for details

## Contact

For questions or issues, please open an issue on the model repository.

---

**Developed for educational and research purposes in mental health technology.**
"""
    return model_card

def upload_to_huggingface():
    """Main function to upload model to Hugging Face"""
    
    print("=" * 70)
    print("Facial Expression Recognition Model - Hugging Face Upload")
    print("=" * 70)
    print()
    
    # Check if model exists
    model_path = "Models/Swin_Transformer/best_model.pth"
    if not os.path.exists(model_path):
        print(f"❌ Error: Model not found at {model_path}")
        print("Please train the model first using: python utilities/train_model.py")
        return
    
    print(f"✅ Model found at: {model_path}")
    print()
    
    # Get Hugging Face token
    print("🔐 Hugging Face Authentication")
    print("-" * 70)
    print("You need a Hugging Face account and access token.")
    print("Get your token from: https://huggingface.co/settings/tokens")
    print()
    
    token = input("Enter your Hugging Face token: ").strip()
    
    if not token:
        print("❌ Error: Token is required")
        return
    
    try:
        # Login to Hugging Face
        print("\n🔄 Logging in to Hugging Face...")
        login(token=token)
        print("✅ Successfully logged in!")
        
    except Exception as e:
        print(f"❌ Login failed: {e}")
        return
    
    # Get repository details
    print("\n📦 Repository Configuration")
    print("-" * 70)
    username = input("Enter your Hugging Face username: ").strip()
    
    if not username:
        print("❌ Error: Username is required")
        return
    
    default_repo_name = "facial-expression-recognition-mental-health"
    repo_name = input(f"Enter repository name (default: {default_repo_name}): ").strip()
    
    if not repo_name:
        repo_name = default_repo_name
    
    repo_id = f"{username}/{repo_name}"
    
    print(f"\n📍 Repository: {repo_id}")
    
    # Create repository
    try:
        print("\n🔄 Creating repository...")
        api = HfApi()
        
        create_repo(
            repo_id=repo_id,
            token=token,
            private=False,
            exist_ok=True
        )
        print(f"✅ Repository created/verified: https://huggingface.co/{repo_id}")
        
    except Exception as e:
        print(f"❌ Failed to create repository: {e}")
        return
    
    # Prepare model info
    model_info = """
- **Optimizer**: AdamW
- **Learning Rate**: 1e-4 with cosine annealing
- **Batch Size**: 32
- **Epochs**: 5
- **Image Size**: 224x224
- **Data Augmentation**: Random horizontal flip, rotation, color jitter
- **Loss Function**: Cross-Entropy Loss
"""
    
    # Create model card
    print("\n📝 Creating model card...")
    model_card_content = create_model_card(repo_id, model_info)
    
    # Save model card locally
    with open("README_HF.md", "w", encoding="utf-8") as f:
        f.write(model_card_content)
    
    print("✅ Model card created: README_HF.md")
    
    # Create config file
    print("\n⚙️ Creating configuration file...")
    config = {
        "model_type": "swin-transformer",
        "architecture": "CustomSwinTransformer",
        "num_classes": 7,
        "emotions": ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"],
        "input_size": [224, 224],
        "framework": "pytorch",
        "license": "mit"
    }
    
    with open("config.json", "w") as f:
        json.dump(config, f, indent=2)
    
    print("✅ Configuration file created: config.json")
    
    # Upload files
    print("\n📤 Uploading files to Hugging Face...")
    print("-" * 70)
    
    try:
        # Upload model
        print("Uploading model file (this may take a few minutes)...")
        api.upload_file(
            path_or_fileobj=model_path,
            path_in_repo="best_model.pth",
            repo_id=repo_id,
            token=token
        )
        print("✅ Model uploaded: best_model.pth")
        
        # Upload README
        print("Uploading model card...")
        api.upload_file(
            path_or_fileobj="README_HF.md",
            path_in_repo="README.md",
            repo_id=repo_id,
            token=token
        )
        print("✅ Model card uploaded: README.md")
        
        # Upload config
        print("Uploading configuration...")
        api.upload_file(
            path_or_fileobj="config.json",
            path_in_repo="config.json",
            repo_id=repo_id,
            token=token
        )
        print("✅ Configuration uploaded: config.json")
        
        print("\n" + "=" * 70)
        print("🎉 SUCCESS! Model uploaded to Hugging Face!")
        print("=" * 70)
        print(f"\n📍 Model URL: https://huggingface.co/{repo_id}")
        print(f"\n💡 To use your model:")
        print(f"   from huggingface_hub import hf_hub_download")
        print(f"   model_path = hf_hub_download(repo_id='{repo_id}', filename='best_model.pth')")
        print("\n✨ Your model is now publicly available!")
        
    except Exception as e:
        print(f"\n❌ Upload failed: {e}")
        return
    
    # Cleanup
    print("\n🧹 Cleaning up temporary files...")
    try:
        os.remove("README_HF.md")
        os.remove("config.json")
        print("✅ Cleanup complete")
    except:
        pass

if __name__ == "__main__":
    try:
        upload_to_huggingface()
    except KeyboardInterrupt:
        print("\n\n⚠️ Upload cancelled by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
