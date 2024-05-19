@echo off
color 0a
Title Batch Scripting Kill Processes
taskkill /f /im notepad.exe
tasklist|findstr notepad.exe || start notepad.exe
pause
