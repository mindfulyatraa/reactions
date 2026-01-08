"""
Quick demo - create 10 second sample with reaction
"""

from viral_video_bot import ViralVideoBot
from pathlib import Path
import sys

# Fix encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

print("Demo: Creating short 10-second reaction video\n")
print("="*50)

# Initialize bot
bot = ViralVideoBot()

if not bot.reaction_videos:
    print("Error: No reaction video found!")
    sys.exit(1)

print(f"Reaction video: {bot.reaction_videos[0]}")

# Check if sample already exists
sample = Path("temp/demo_viral.mp4")

if not sample.exists():
    print("\nPlease wait - downloading sample...")
    import requests
    
    # Smaller, shorter sample video
    url = "https://www.w3schools.com/html/mov_bbb.mp4"
    
    try:
        r = requests.get(url, timeout=30)
        sample.parent.mkdir(exist_ok=True)
        sample.write_bytes(r.content)
        print("Download complete!")
    except Exception as e:
        print(f"Download failed: {e}")
        sys.exit(1)
else:
    print(f"\nUsing existing sample: {sample}")

# Create demo
output = Path("output_videos/DEMO_reaction.mp4")
output.parent.mkdir(exist_ok=True)

print("\nProcessing video...")
print("- Adding your reaction (top 40%)")
print("- Adding viral content (bottom 60%)")
print("- Adding text: 'Wait for it...'")
print("\nPlease wait (this takes 1-2 minutes)...\n")

success = bot.create_reaction_video(
    str(sample),
    bot.reaction_videos[0],
    str(output)
)

if success:
    print("\n" + "="*50)
    print("SUCCESS! Demo video created!")
    print("="*50)
    print(f"\nLocation: {output.absolute()}")
    print(f"Size: {output.stat().st_size / (1024*1024):.1f} MB")
    print("\nOpen 'output_videos' folder to watch it!")
else:
    print("\nFailed to create video. Check viral_bot.log for details.")
