::File name with date and time [YYYYMMDDHHMMSSMS]
echo off
color E
set A=%date:~10,4%%date:~4,2%%date:~7,2%
echo %A%
set B=%time:~0,2%%time:~3,2%%time%%time:~9,2%
echo %B%
set /p C=Enter Directory Path:
mkdir %C%%A%%B: =%
pause