"""
Batch processing script for GitHub Actions
"""
from viral_video_bot import ViralVideoBot
import logging
import time
import sys
import os

# Configure logging
logging.basicConfig(level=logging.INFO)

def run_batch():
    print("Starting Batch Process...")
    
    bot = ViralVideoBot()
    
    # Debug: Check reaction videos
    logging.info(f"Checking reaction directory: {bot.config.get('reaction_dir')}")
    if os.path.exists(bot.config.get('reaction_dir')):
        files = os.listdir(bot.config.get('reaction_dir'))
        logging.info(f"Files in reaction dir: {files}")
    else:
        logging.error("Reaction directory does not exist!")

    # Search for viral videos with fallback mechanism
    viral_videos = []
    sources_to_try = ['reddit', 'youtube', 'instagram']  # Priority order

    for source in sources_to_try:
        logging.info(f"Trying to search viral videos on {source}...")

        try:
            if source == 'youtube':
                videos = bot.search_viral_videos_youtube()
            elif source == 'instagram':
                videos = bot.search_viral_videos_instagram()
            else:  # reddit
                videos = bot.search_viral_videos_reddit()

            if videos:
                viral_videos = videos
                logging.info(f"Found {len(viral_videos)} videos from {source}")
                break  # Stop trying other sources if we found videos
            else:
                logging.warning(f"No videos found from {source}, trying next source...")

        except Exception as e:
            logging.error(f"Error searching {source}: {str(e)}")
            continue  # Try next source

    if not viral_videos:
        logging.error("No new viral videos found from any source.")
        sys.exit(1) # Force fail
    
    logging.info(f"Found {len(viral_videos)} potential videos")
    
    # Process
    count = 0
    for video_info in viral_videos:
        if count >= 1: 
            break
            
        logging.info(f"Processing candidate: {video_info['title']}")
        success = bot.process_viral_video(video_info)
        
        if success:
            count += 1
            logging.info("Video processed and uploaded successfully!")
        else:
            logging.error(f"Failed to process video: {video_info['title']}")
            
    logging.info(f"Batch complete. Processed {count} videos.")
    
    if count == 0:
        logging.error("Batch finished with 0 processed videos.")
        sys.exit(1) # Force fail if nothing happened()

if __name__ == "__main__":
    run_batch()
