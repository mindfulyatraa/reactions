"""
Simple test script to create a single reaction video
Ye script use karke ek test video bana sakte ho
"""

from viral_video_bot import ViralVideoBot
from pathlib import Path
import logging
import sys

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Setup logging
logging.basicConfig(level=logging.INFO)

def test_create_video():
    """Test video creation with local files"""
    
    print("Starting test video creation...")
    
    
    # Initialize bot
    bot = ViralVideoBot()
    
    # Check if reaction video exists
    reaction_videos = bot.reaction_videos
    if not reaction_videos:
        print("Error: No reaction videos found!")
        print("Please add your reaction video to 'reaction_videos/' folder")
        return False
    
    print(f"Found {len(reaction_videos)} reaction video(s)")
    
    # For testing, you need to manually download a viral video first
    # Or use the full bot to auto-download from Reddit
    
    print("\nTest Options:")
    print("Option 1: Run full bot to auto-download and process")
    print("   Command: py viral_video_bot.py")
    print("\nOption 2: Test with specific files")
    print("   1. Download a viral video manually")
    print("   2. Place it in 'temp/' folder as 'test_viral.mp4'")
    print("   3. Run this script again")
    
    # Check if test viral video exists
    test_viral = Path("temp/test_viral.mp4")
    if test_viral.exists():
        print(f"\nFound test viral video: {test_viral}")
        
        # Create output
        output = Path("output_videos/test_output.mp4")
        
        print("\nCreating reaction video...")
        success = bot.create_reaction_video(
            str(test_viral),
            reaction_videos[0],
            str(output)
        )
        
        if success:
            print(f"\nSUCCESS! Video created: {output}")
            print("Check the output_videos/ folder!")
            return True
        else:
            print("\nFailed to create video. Check logs for details.")
            return False
    else:
        print(f"\nTest viral video not found at: {test_viral}")
        print("Download a short MP4 video and save it as 'temp/test_viral.mp4'")
        
        # Create temp directory if it doesn't exist
        Path("temp").mkdir(exist_ok=True)
        
    return False


if __name__ == "__main__":
    test_create_video()
