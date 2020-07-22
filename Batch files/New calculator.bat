@echo off
title Batch Calculator by Neeraj
color 1f
:top
echo --------------------------------------------------------------
echo Welcome to Batch Calculator by Neeraj
echo --------------------------------------------------------------
echo.
set /p sum=
set /a ans=%sum%
echo.
echo = %ans%
echo --------------------------------------------------------------
pause
cls
echo Previous Question: %sum%
echo Previous Answer: %ans%
goto top
pause
exit
