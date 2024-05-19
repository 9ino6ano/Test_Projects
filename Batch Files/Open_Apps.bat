@echo off
Title Open_Application
pause
start "C:\Program Files\Git\git-bash.exe" --cd-to-home
start /d %windir%\system32\mspaint.exe
start notepad
exit