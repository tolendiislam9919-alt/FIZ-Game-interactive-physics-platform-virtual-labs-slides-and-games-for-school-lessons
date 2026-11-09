@echo off
chcp 65001 >nul
title FIZ Game
cd /d "%~dp0"
python server.py
if errorlevel 1 (
  echo.
  echo Python табылмады. python.org сайтынан орнатыңыз немесе index.html файлын жай ашыңыз.
  pause
)
