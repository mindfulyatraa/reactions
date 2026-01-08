@echo off
echo ===================================================
echo   YouTube Authentication & Test Upload
echo ===================================================
echo.
echo This script will:
echo 1. Open your browser for Google Login
echo 2. Authenticate the Viral Video Bot
echo 3. Automatically upload the DEMO video
echo.
echo NOTE: If you see "App not verified", click:
echo Advanced > Go to Viral Video Bot (unsafe)
echo.
pause

py youtube_uploader.py

pause
