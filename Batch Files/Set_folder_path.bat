@echo off
Title Make_a_folder
echo Building a batch script, asking the user for the folder path and the name of the folder
mkdir "C:\Users\Pana\Downloads\Documents"
echo *N.B This is the primary directory of the folder.
set /p folder_name=Enter the new folder name:
set /p folder_path=Enter the new folder path:
set new_path=%folder_path%\%folder_name%
echo You will be saving the new folder @ %new_path%
mkdir %new_path%
pause