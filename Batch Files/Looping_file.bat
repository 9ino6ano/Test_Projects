@echo off
Title Looping_through_a_file
set /p folder_path=Enter the folder path:
cd %folder_path%
for %%i in (*.*) do echo %%i
pause
