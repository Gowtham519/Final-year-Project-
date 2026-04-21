@echo off
echo Starting Rice Quality Analysis System...

:: Start Backend
echo Starting Backend Server...
start "Rice Backend" cmd /k "cd Backend && "C:\Users\Gude Pavan Kumar\AppData\Local\Programs\Python\Python311\python.exe" main.py"

:: Wait a moment for backend to initialize
timeout /t 5 /nobreak

:: Start Frontend
echo Starting Frontend Server...
start "Rice Frontend" cmd /k "cd frontend && "C:\Program Files\nodejs\npm.cmd" run dev"

echo System started! Checks the open windows for any errors.
