"""
Download Trained Model from Hugging Face
This script automatically downloads the facial expression recognition model
"""

import os
from huggingface_hub import hf_hub_download
from pathlib import Path

def download_model_from_huggingface():
    """Download the trained model from Hugging Face Hub"""
    
    print("=" * 70)
    print("Facial Expression Recognition Model - Download from Hugging Face")
    print("=" * 70)
    print()
    
    # Model repository information
    print("📦 Model Repository Information")
    print("-" * 70)
    print("Please provide your Hugging Face model repository details.")
    print("Format: username/repository-name")
    print("Example: john-doe/facial-expression-recognition-mental-health")
    print()
    
    # Get repository ID from user
    repo_id = input("Enter your Hugging Face repository ID: ").strip()
    
    if not repo_id:
        print("❌ Error: Repository ID is required")
        return False
    
    # Validate format
    if "/" not in repo_id:
        print("❌ Error: Invalid format. Use 'username/repository-name'")
        return False
    
    # Create Models directory if it doesn't exist
    model_dir = Path("Models/Swin_Transformer")
    model_dir.mkdir(parents=True, exist_ok=True)
    
    model_path = model_dir / "best_model.pth"
    
    # Check if model already exists
    if model_path.exists():
        print(f"\n⚠️  Model already exists at: {model_path}")
        overwrite = input("Do you want to re-download? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("✅ Using existing model")
            return True
    
    try:
        print(f"\n🔄 Downloading model from: {repo_id}")
        print("This may take a few minutes depending on your internet connection...")
        print("-" * 70)
        
        # Download the model
        downloaded_path = hf_hub_download(
            repo_id=repo_id,
            filename="best_model.pth",
            cache_dir=".cache",
            local_dir="Models/Swin_Transformer",
            local_dir_use_symlinks=False
        )
        
        print("\n" + "=" * 70)
        print("🎉 SUCCESS! Model downloaded successfully!")
        print("=" * 70)
        print(f"\n📍 Model saved to: {model_path}")
        print(f"📊 Model size: {model_path.stat().st_size / (1024*1024):.2f} MB")
        print("\n✅ You can now run the web application with: python web_app.py")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Download failed: {e}")
        print("\nPossible reasons:")
        print("1. Invalid repository ID")
        print("2. Model file not found in repository")
        print("3. Repository is private (make sure it's public)")
        print("4. Network connection issues")
        print("\nPlease check and try again.")
        return False

def quick_download(repo_id):
    """Quick download with pre-configured repository ID"""
    
    model_dir = Path("Models/Swin_Transformer")
    model_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        print(f"Downloading model from {repo_id}...")
        hf_hub_download(
            repo_id=repo_id,
            filename="best_model.pth",
            cache_dir=".cache",
            local_dir="Models/Swin_Transformer",
            local_dir_use_symlinks=False
        )
        print("✅ Model downloaded successfully!")
        return True
    except Exception as e:
        print(f"❌ Download failed: {e}")
        return False

if __name__ == "__main__":
    try:
        download_model_from_huggingface()
    except KeyboardInterrupt:
        print("\n\n⚠️ Download cancelled by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
