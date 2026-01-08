# 🎬 Viral Video Reaction Bot

An automated bot that finds viral videos from Reddit, adds reaction overlays, and uploads them to YouTube and TikTok.

## 🌟 Features

- **Automated Video Discovery**: Searches Reddit for trending viral videos
- **Reaction Video Creation**: Combines viral videos with reaction footage in split-screen layout
- **Multi-Platform Upload**: Automatically uploads to YouTube and TikTok
- **Smart Processing**: Tracks processed videos to avoid duplicates
- **Configurable**: Easy JSON-based configuration
- **24/7 Operation**: Runs continuously with scheduled checks

## 📋 Prerequisites

1. **Python 3.8+**
2. **FFmpeg** - Required for video processing
   - Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html)
   - Add FFmpeg to your system PATH

## 🚀 Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Add Reaction Videos

Create a `reaction_videos` folder and add your reaction video clips (*.mp4 files):

```
last project/
├── reaction_videos/
│   ├── reaction1.mp4
│   ├── reaction2.mp4
│   └── reaction3.mp4
```

### 3. Configure Settings

Edit `config.json` to customize:

- **search_keywords**: Keywords for finding viral content
- **min_views**: Minimum views required (default: 100,000)
- **max_video_duration**: Maximum video length in seconds
- **check_interval_minutes**: How often to check for new videos
- **reddit_subreddits**: Which subreddits to search

### 4. YouTube API Setup (Optional)

To enable YouTube uploads:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable YouTube Data API v3
4. Create OAuth 2.0 credentials
5. Download `client_secrets.json` to project directory

### 5. TikTok API Setup (Optional)

To enable TikTok uploads:

1. Register for TikTok Developer account
2. Create an app and get API credentials
3. Add credentials to the upload function

## 🎮 Usage

### Run the Bot

```bash
python viral_video_bot.py
```

The bot will:
1. Search Reddit for viral videos every 30 minutes (configurable)
2. Download videos that meet the criteria
3. Combine them with random reaction videos
4. Upload to configured platforms
5. Log all activities to `viral_bot.log`

### Stop the Bot

Press `Ctrl+C` to stop the bot gracefully.

## 📁 Project Structure

```
last project/
├── viral_video_bot.py      # Main bot script
├── config.json              # Configuration file
├── requirements.txt         # Python dependencies
├── processed_videos.json    # Tracks processed videos
├── viral_bot.log           # Activity log
├── reaction_videos/        # Your reaction video clips
├── output_videos/          # Generated reaction videos
└── temp/                   # Temporary downloads
```

## ⚙️ Configuration Options

| Option | Description | Default |
|--------|-------------|---------|
| `search_keywords` | Keywords for viral content search | `["funny pets", "viral funny", ...]` |
| `min_views` | Minimum view count threshold | `100000` |
| `max_video_duration` | Max video length (seconds) | `60` |
| `check_interval_minutes` | Search interval | `30` |
| `output_dir` | Output directory for videos | `"output_videos"` |
| `reaction_dir` | Directory with reaction clips | `"reaction_videos"` |
| `upload_platforms` | Platforms to upload to | `["youtube", "tiktok"]` |
| `reddit_subreddits` | Subreddits to search | `["funny", "aww", ...]` |
| `video_quality` | Output video quality | `"720p"` |

## 🎥 Video Output Format

- **Resolution**: 720x1280 (vertical format for shorts/reels)
- **Layout**: Split-screen with original video on top (70%) and reaction on bottom (30%)
- **Codec**: H.264 (MP4)
- **Audio**: AAC
- **FPS**: 30

## 📊 Logs

All bot activities are logged to `viral_bot.log`:
- Video discoveries
- Downloads
- Processing status
- Upload results
- Errors and warnings

## ⚠️ Important Notes

1. **Reaction Videos**: Add at least one reaction video to `reaction_videos/` folder before running
2. **Reddit Rate Limits**: The bot respects Reddit's rate limits with delays
3. **API Credentials**: YouTube/TikTok uploads require proper API setup
4. **Copyright**: Ensure you have rights to use discovered content
5. **Storage**: Monitor disk space as videos can accumulate

## 🛠️ Troubleshooting

**"No reaction videos available"**
- Add MP4 files to the `reaction_videos/` folder

**"FFmpeg not found"**
- Install FFmpeg and add it to your system PATH

**YouTube upload not working**
- Set up `client_secrets.json` with valid OAuth credentials
- Complete the OAuth flow on first run

**Videos not downloading**
- Check your internet connection
- Verify Reddit API is accessible
- Lower `min_views` threshold in config

## 📝 License

This project is for educational purposes. Respect copyright laws and platform terms of service.

## 🤝 Contributing

Feel free to fork, modify, and improve this bot!

---

**Made with ❤️ for content creators**
