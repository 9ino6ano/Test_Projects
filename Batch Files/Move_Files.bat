@echo off
Title Move_File
pause
echo I want to move a file from one folder to another folder
move "C:\Users\Pana\Downloads\Documents\Resume_Template.docx" "C:\Users\Pana\OneDrive\Pictures\Saved Pictures"
pause
echo I want to move multiple files ending in docx. to another folder
move "C:\Users\Pana\Downloads\Documents\*.docx" "C:\Users\Pana\Documents\Projects"