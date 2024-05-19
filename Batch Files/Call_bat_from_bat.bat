::Caliing another bat file from a bat file
@echo off
set /p A=Enter Name:
set /p B=Enter Surname:
call C:\Users\Lebo Kgaswane\Documents\Batch_Scripts\Test.bat %A% %B%
echo Returned to main!!
pause
