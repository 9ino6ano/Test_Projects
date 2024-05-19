@echo off
color 0a
Title Batch Scripting Timeout before Killing a Processes
start notepad /t 10 /nobreak
taskkill /f /im notepad.exe
pause