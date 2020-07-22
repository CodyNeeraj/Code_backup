@echo off
title hahaha
mode con: cols=40 lines=20
color 0a
echo Hello world !
echo time is=%time%
echo date is %date%
echo.
set /p sum=
set /a ans=%sum%
echo.
echo = %ans%
echo previous answer= %ans%

pause