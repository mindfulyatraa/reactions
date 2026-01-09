# Reddit Authentication Setup Guide

## 📋 Prerequisites

Reddit videos download karne ke liye aapko Reddit account credentials chahiye.

## 🔧 Setup Steps

### Step 1: Reddit Account Create/Use

1. **Reddit account** banao ya existing use karo
2. **2FA disable** karo temporarily (optional, but easier setup ke liye)

### Step 2: GitHub Secrets Setup

GitHub repository ke **Settings > Secrets and variables > Actions** mein jao:

1. **New repository secret** click karo
2. **Name**: `REDDIT_USERNAME`
3. **Value**: Aapka Reddit username
4. **Add secret** click karo

5. **New repository secret** dobara banao
6. **Name**: `REDDIT_PASSWORD`
7. **Value**: Aapka Reddit password
8. **Add secret** click karo

### Step 3: Local Testing (Optional)

Agar local pe test karna hai:

```bash
# Environment variables set karo
export REDDIT_USERNAME="your_username"
export REDDIT_PASSWORD="your_password"

# Test run
python run_batch.py
```

---

## 🎬 Test Download

Reddit download test karne ke liye:

```bash
python test_reddit_ytdlp.py
```

Ye Reddit se video download karne ka test karega.

---

## ⚙️ Bot Configuration

`config.json` mein Reddit source enable karo:

```json
{
  "source_platform": "reddit",
  "reddit_subreddits": [
    "funny",
    "aww",
    "unexpected",
    "PublicFreakout"
  ],
  ...
}
```

---

## 🚀 Automatic Download

Jab bot run hoga, automatically Reddit se videos download karega!

Bot automatically:
- ✅ Reddit RSS feeds se viral videos find karega
- ✅ Authentication use karke videos download karega
- ✅ Reaction videos ke saath combine karega
- ✅ YouTube pe upload karega

---

## 📝 Important Notes

1. **Rate Limits**: Reddit API ka limit hai (~600 requests/hour)
2. **Content Policy**: Reddit community guidelines follow karo
3. **Copyright**: Fair use ke liye proper credit do
4. **Authentication**: Username/password secure rakhna

---

## ❓ Troubleshooting

**"Reddit credentials not found"**
→ GitHub secrets properly set karo ya environment variables check karo

**"Authentication failed"**
→ Username/password correct hai ya nahi check karo
→ 2FA enabled hai to disable karo

**"Rate limit exceeded"**
→ Thoda wait karo, automatically reset hoga

---

## 🔐 Security

- ⚠️ **Never share** Reddit credentials publicly
- ⚠️ **Never commit** passwords to GitHub
- ✅ GitHub secrets use karo production mein
- ✅ Environment variables use karo local testing mein