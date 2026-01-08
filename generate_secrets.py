import pickle
import base64
import json
import os

print("\n" + "="*80)
print("GITHUB SECRETS GENERATOR")
print("="*80)
print("Copy values below and add them to:")
print("Repo Settings > Secrets and variables > Actions > New repository secret\n")

# 1. Client Secrets
if os.path.exists('client_secrets.json'):
    with open('client_secrets.json', 'r') as f:
        content = f.read()
        print("-" * 20)
        print("SECRET NAME:  YOUTUBE_CLIENT_SECRETS")
        print("-" * 20)
        print(content)
        print("\n")
else:
    print("❌ client_secrets.json not found!")

# 2. Token Pickle (Base64 Encoded)
if os.path.exists('youtube_token.pickle'):
    with open('youtube_token.pickle', 'rb') as f:
        token_data = f.read()
        b64_token = base64.b64encode(token_data).decode('utf-8')
        print("-" * 20)
        print("SECRET NAME:  YOUTUBE_TOKEN_PICKLE")
        print("-" * 20)
        print(b64_token)
        print("\n")
else:
    print("❌ youtube_token.pickle not found! Run SETUP_YOUTUBE.bat first.")

print("="*80)
print("Done! Add these 2 secrets to GitHub to make automation work.")
print("="*80)
