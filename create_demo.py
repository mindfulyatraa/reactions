"""
Quick demo script to create a sample reaction video
"""

from viral_video_bot import ViralVideoBot
from pathlib import Path
import requests
import logging
import sys

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

logging.basicConfig(level=logging.INFO)

def download_sample_video():
    """Download a sample short video for demo"""
    print("Downloading sample video for demo...")
    
    # Using a short sample video URL (Big Buck Bunny - open source)
    sample_url = "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
    
    output_path = Path("temp/demo_viral.mp4")
    output_path.parent.mkdir(exist_ok=True)
    
    try:
        response = requests.get(sample_url, stream=True, timeout=30)
        
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"Sample video downloaded to: {output_path}")
            return output_path
        else:
            print(f"Failed to download. Status: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Error downloading: {e}")
        return None

def create_demo_video():
    """Create a demo reaction video"""
    print("\n" + "="*50)
    print("Creating Demo Reaction Video")
    print("="*50 + "\n")
    
    # Initialize bot
    bot = ViralVideoBot()
    
    # Check reaction video
    if not bot.reaction_videos:
        print("Error: No reaction videos found!")
        return False
    
    print(f"Using reaction video: {bot.reaction_videos[0]}")
    
    # Download sample video
    sample_video = download_sample_video()
    
    if not sample_video:
        print("Failed to download sample video")
        return False
    
    # Create output path
    output = Path("output_videos/DEMO_reaction_video.mp4")
    output.parent.mkdir(exist_ok=True)
    
    print("\nCreating reaction video with:")
    print(f"  - Your reaction (top 40%)")
    print(f"  - Viral content (bottom 60%)")
    print(f"  - Text overlay: 'Wait for it...'")
    print("\nThis may take a few minutes...\n")
    
    # Create the reaction video
    success = bot.create_reaction_video(
        str(sample_video),
        bot.reaction_videos[0],
        str(output)
    )
    
    if success:
        print("\n" + "="*50)
        print("SUCCESS!")
        print("="*50)
        print(f"\nDemo video created: {output}")
        print(f"File size: {output.stat().st_size / 1024 / 1024:.2f} MB")
        print("\nOpen the 'output_videos' folder to watch it!")
        return True
    else:
        print("\nFailed to create video")
        return False

if __name__ == "__main__":
    create_demo_video()

def download_sample_video():
    """Download a sample short video for demo"""
    print("Downloading sample video for demo...")
    
    # Using a short sample video URL (Big Buck Bunny - open source)
    sample_url = "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
    
    output_path = Path("temp/demo_viral.mp4")
    output_path.parent.mkdir(exist_ok=True)
    
    try:
        response = requests.get(sample_url, stream=True, timeout=30)
        
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"Sample video downloaded to: {output_path}")
            return output_path
        else:
            print(f"Failed to download. Status: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Error downloading: {e}")
        return None

def create_demo_video():
    """Create a demo reaction video"""
    print("\n" + "="*50)
    print("Creating Demo Reaction Video")
    print("="*50 + "\n")
    
    # Initialize bot
    bot = ViralVideoBot()
    
    # Check reaction video
    if not bot.reaction_videos:
        print("Error: No reaction videos found!")
        return False
    
    print(f"Using reaction video: {bot.reaction_videos[0]}")
    
    # Download sample video
    sample_video = download_sample_video()
    
    if not sample_video:
        print("Failed to download sample video")
        return False
    
    # Create output path
    output = Path("output_videos/DEMO_reaction_video.mp4")
    output.parent.mkdir(exist_ok=True)
    
    print("\nCreating reaction video with:")
    print(f"  - Your reaction (top 40%)")
    print(f"  - Viral content (bottom 60%)")
    print(f"  - Text overlay: 'Wait for it... 😂'")
    print("\nThis may take a few minutes...\n")
    
    # Create the reaction video
    success = bot.create_reaction_video(
        str(sample_video),
        bot.reaction_videos[0],
        str(output)
    )
    
    if success:
        print("\n" + "="*50)
        print("SUCCESS!")
        print("="*50)
        print(f"\nDemo video created: {output}")
        print(f"File size: {output.stat().st_size / 1024 / 1024:.2f} MB")
        print("\nOpen the 'output_videos' folder to watch it!")
        return True
    else:
        print("\nFailed to create video")
        return False

if __name__ == "__main__":
    create_demo_video()
