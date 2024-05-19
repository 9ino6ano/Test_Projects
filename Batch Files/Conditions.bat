@echo off
:start
cls
set /p user_input=Do you like to continue (Y/N)?:
if not defined user_input goto start
if /i %user_input%==y goto Yes
if /i %user_input%--n (goto No) else (goto Invalid)

:Yes
echo The user has chosen yes
pause
goto start

:No
echo The user has chosen no
pause
exit

:Invalid
echo %user_input% is an invalid value, Please try again!!
set user_input=
pause
goto start