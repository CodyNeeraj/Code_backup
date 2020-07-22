@echo off
:calc
cls
color e4
title SIMPLE CALCULATOR

echo 1.Add                  +
echo 2.Subtract             -
echo 3.Multiply             *
echo 4.Divide               /
echo Put your question 
set/p equ=
set/a equ=!equ! 
echo Answer=!equ! 
pause
goto calc


