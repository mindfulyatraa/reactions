# 🎬 Quick Start Guide - Viral Video Bot

## 📝 Aapne jo changes request kiye the:

✅ **Text Overlay**: Har video pe "Wait for it... 😂" automatically add hoga  
✅ **Layout Reversed**: Upar aapki reaction video, neeche viral video  
✅ **Auto-Looping**: Aapki 30-second reaction video automatically viral video ke duration ke according loop hogi  
✅ **Perfect Template**: Reference image jaisa exact style  

---

## 🚀 Setup Steps (Ek baar karna hai)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

> **Note**: Agar `moviepy` ya `Pillow` install mein koi error aaye toh manually install karein:
```bash
pip install moviepy Pillow
```

### 2. Install FFmpeg (Important!)

**Windows:**
1. Download: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip
2. Extract kar do `C:\ffmpeg` mein
3. System Environment Variables mein add karo:
   - Path: `C:\ffmpeg\bin`

Test karo:
```bash
ffmpeg -version
```

### 3. Add Your Reaction Video

Apni reaction video (30 seconds wali) ko `reaction_videos` folder mein daalo:

```
last project/
├── reaction_videos/
│   └── my_reaction.mp4    ← Aapki reaction video yahan
```

---

## 🎮 Usage - Bot Kaise Chalaye

### Option 1: Automatic Mode (24/7)

Bot automatically har 30 minutes mein Reddit check karega aur videos banayega:

```bash
python viral_video_bot.py
```

Bot kya karega:
1. ✅ Reddit se viral videos dhundhega
2. ✅ Videos download karega
3. ✅ Aapki reaction video upar add karega
4. ✅ "Wait for it... 😂" text overlay lagayega
5. ✅ Final video `output_videos/` folder mein save karega
6. ✅ YouTube/TikTok pe upload karega (agar API setup hai)

**Stop karne ke liye**: `Ctrl + C` press karo

---

### Option 2: Manual Testing (Single Video)

Pehle test karna chahte ho? Ye simple script use karo:

**Create file: `test_single_video.py`**

```python
from viral_video_bot import ViralVideoBot
from pathlib import Path

# Bot initialize karo
bot = ViralVideoBot()

# Test video info (example)
test_video = {
    'id': 'test123',
    'title': 'Hilarious Comedy',
    'url': 'https://v.redd.it/your-video-url/DASH_720.mp4',
    'score': 150000,
    'source': 'reddit',
    'subreddit': 'funny'
}

# Process karo
print("Creating reaction video...")
success = bot.process_viral_video(test_video)

if success:
    print("✅ Video successfully created in output_videos/ folder!")
else:
    print("❌ Error occurred")
```

Run karo:
```bash
python test_single_video.py
```

---

## ⚙️ Configuration Customization

`config.json` file mein settings change kar sakte ho:

### Text Overlay Customize Karo

```json
"text_overlay": {
    "enabled": true,
    "text": "Wait for it... 😂",    ← Ye text change kar sakte ho
    "font_size": 70,                ← Text size badhao/ghatao
    "font_color": "white",          ← Color change karo
    "stroke_color": "black",        ← Outline color
    "stroke_width": 4,              ← Outline thickness
    "position_top": 80              ← Text ki position (pixels)
}
```

### Video Layout Adjust Karo

```json
"video_layout": {
    "reaction_top_percent": 40,     ← Reaction video ka size (%)
    "viral_bottom_percent": 60      ← Viral video ka size (%)
}
```

### Search Settings

```json
"min_views": 100000,                ← Minimum views required
"max_video_duration": 60,           ← Max video length (seconds)
"check_interval_minutes": 30,       ← Kitne minutes baad check kare
```

---

## 📂 Folder Structure

```
last project/
├── viral_video_bot.py          # Main bot
├── config.json                  # Settings
├── requirements.txt             # Dependencies
├── processed_videos.json        # Tracked videos
├── viral_bot.log               # Activity logs
│
├── reaction_videos/            # Aapki reaction videos
│   └── my_reaction.mp4
│
├── output_videos/              # Final created videos
│   └── reaction_20260108_183000.mp4
│
└── temp/                       # Temporary downloads
```

---

## 🎨 Video Output Specs

- **Format**: MP4 (H.264)
- **Resolution**: 720x1280 (9:16 vertical)
- **FPS**: 30
- **Audio**: AAC
- **Layout**:
  - Top 40%: Aapki reaction video
  - Bottom 60%: Viral video
  - Text overlay: "Wait for it... 😂" (top-center)

---

## 🔧 Troubleshooting

### "No reaction videos available!"
➡️ `reaction_videos/` folder mein apni .mp4 file daalo

### "FFmpeg not found"
➡️ FFmpeg install karo aur system PATH mein add karo

### Text rendering error
➡️ Ye command run karo:
```bash
pip install Pillow --upgrade
```

### Video processing slow hai
➡️ `config.json` mein `max_video_duration` kam kar do (e.g., 30 seconds)

---

## 📊 Logs Check Karo

Bot ki activity dekhni hai? `viral_bot.log` file open karo:

```bash
type viral_bot.log
```

Ya real-time dekhna hai:
```bash
Get-Content viral_bot.log -Wait
```

---

## 🎯 Quick Commands Cheat Sheet

| Command | Kya Karega |
|---------|------------|
| `python viral_video_bot.py` | Bot start karo (24/7 mode) |
| `Ctrl + C` | Bot stop karo |
| `pip install -r requirements.txt` | Dependencies install karo |
| `ffmpeg -version` | FFmpeg check karo |
| `type viral_bot.log` | Logs dekho |

---

## ✨ Tips for Best Results

1. **High Quality Reaction**: Aapki reaction video clear aur engaging honi chahiye
2. **Good Lighting**: Reaction video mein proper lighting ho
3. **Audio Check**: Reaction video ka audio clear ho
4. **Regular Monitoring**: Logs regularly check karo for any errors
5. **Storage**: Output videos ka backup rakho

---

## 🚨 Important Notes

> **Copyright**: Viral videos use karne se pehle copyright rules check karo  
> **API Setup**: YouTube/TikTok upload ke liye API credentials chahiye  
> **Storage**: Videos jald space le sakte hain, regular cleanup karo  

---

**Bot ready hai! Abhi apni reaction video daalo aur testing shuru karo! 🎬✨**
