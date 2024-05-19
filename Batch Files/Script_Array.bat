@echo off
color 0a
Title Batch Script Array Example
set A=9ino 6ano 9ana6y
for %%b in (%A%) do (
echo %%b
echo Here are the winners..
timeout /t 5 /nobreak
)
pause
