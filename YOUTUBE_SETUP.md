# YouTube Upload Setup Guide

## 📋 Prerequisites

YouTube upload ke liye aapko Google Cloud Console se OAuth credentials chahiye.

## 🔧 Setup Steps

### Step 1: Google Cloud Console Setup

1. **Go to**: https://console.cloud.google.com/
2. **Create new project** ya existing project select karo
3. **Enable YouTube Data API v3**:
   - APIs & Services > Library
   - Search "YouTube Data API v3"
   - Click "Enable"

### Step 2: Create OAuth Credentials

1. **APIs & Services > Credentials**
2. **Create Credentials > OAuth client ID**
3. **Application type**: Desktop app
4. **Name**: Viral Video Bot
5. **Download JSON** file

### Step 3: Configure Bot

1. Downloaded JSON file ko **rename** karo: `client_secrets.json`
2. File ko project folder mein copy karo:
   ```
   last project/
   ├── client_secrets.json  ← Yahan paste karo
   ├── viral_video_bot.py
   └── ...
   ```

### Step 4: First Time Authentication

Jab bot pehli baar run hoga:
1. Browser automatically kh ulega
2. Google account se login karo
3. Permissions allow karo
4. Authentication complete!

Bot automatically credentials save kar lega `youtube_token.pickle` mein.

---

## 🎬 Test Upload

Test upload karne ke liye:

```bash
py youtube_uploader.py
```

Ye demo video upload karega YouTube pe (confirmation mangega).

---

## ⚙️ Bot Configuration

`config.json` mein YouTube upload enable karo:

```json
{
  "upload_platforms": ["youtube"],
  ...
}
```

---

## 🚀 Automatic Upload

Jab bot viral videos process karega, automatically YouTube pe upload ho jayengi!

Bot automatically:
- ✅ Catchy title generate karega
- ✅ Description add karega with hashtags
- ✅ "Shorts" format mein upload karega
- ✅ Public visibility set karega

---

## 📝 Important Notes

1. **API Quota**: YouTube API ka daily limit hai (~10,000 units/day)
2. **Upload Limit**: ~6 uploads per day is safe
3. **Content Policy**: YouTube community guidelines follow karo
4. **Copyright**: Fair use ke liye proper credit do

---

## ❓ Troubleshooting

**"client_secrets.json not found"**
→ OAuth credentials download karke paste karo

**"Quota exceeded"**
→ 24 hours wait karo, quota reset ho jayega

**"Authentication failed"**
→ `youtube_token.pickle` delete karke dobara authenticate karo

---

## 🔐 Security

- ⚠️ **Never share** `client_secrets.json` publicly
- ⚠️ **Never commit** credentials to GitHub
- ✅ Already added to `.gitignore`
