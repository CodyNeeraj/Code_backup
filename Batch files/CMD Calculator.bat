@echo off
color 3f
title  Neeraj

 :start
echo Press 1 to Add
echo Press 2 to Subtract
echo Press 3 to Multiply
echo Press 4 to Divide
echo Press 5 to Quit
set /p type=
if %type%==1 goto a
if %type%==2 goto b
if %type%==3 goto c
if %type%==4 goto d
if %type%==5 goto e
 :a
echo Addition
echo Please choose the 3 numbers you wish to add
set /p num1=
set /p num2=
set /p num3=
echo %num1%+%num2%+%num3%
pause
set /a Answer=%num1%+%num2%+%num3%
echo %Answer%
pause
goto start
 :b
echo Subtraction
echo Please choose the 2 numbers you wish to subtract
set /p num1=
set /p num2=
echo %num1%-%num2%
pause
set /a Answer=%num1%-%num2%
echo %Answer%
pause
goto start
 :c
echo Multiplication
echo Please choose the 2 numbers you wish to multiply
set /p num1=
set /p num2=
echo %num1%*%num2%
pause
set /a Answer=%num1%*%num2%
echo %Answer%
pause
goto start
 :d
echo Division
echo Please choose the 2 numbers you wish to divide
set /p num1=
set /p num2=
echo %num1%/%num2%
pause
set /a Answer=%num1%/%num2%
echo %Answer%
pause
goto start
 :e
echo. Done!