@echo off
Title Open URL
echo This will open daily used urls in private/incognito
pause
start /d "C:\Program Files\Google\Chrome\Application" chrome.exe -incognito https://www.google.com
start msedge.exe -inprivate https://www.youtube.com