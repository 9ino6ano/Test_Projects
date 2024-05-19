@echo off
Title Batch_Script_For User Input In Variable
:start
cls
set /p input=Enter the Name:
echo %input%, We are delighted to have you at the event!!
pause
goto start