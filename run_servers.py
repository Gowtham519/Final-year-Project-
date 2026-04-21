import subprocess
import os
import time

# Absolute paths
PYTHON_EXE = r"C:\Users\Gude Pavan Kumar\AppData\Local\Programs\Python\Python311\python.exe"
NPM_CMD = r"C:\Program Files\nodejs\npm.cmd"

# Directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, "Backend")
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

# Update PATH to include Node.js and Python
os.environ["PATH"] = r"C:\Program Files\nodejs;" + r"C:\Users\Gude Pavan Kumar\AppData\Local\Programs\Python\Python311;" + r"C:\Users\Gude Pavan Kumar\AppData\Local\Programs\Python\Python311\Scripts;" + os.environ["PATH"]

print("Launching Rice Quality Analysis servers...")

# Launch Backend
print("Starting Backend...")
# We use start command via shell=True to open new windows
# Note: we don't need absolute path to python/npm anymore if they are in PATH, but keeping them is safe.
subprocess.Popen(
    f'start "Rice Backend" cmd /k "cd /d "{BACKEND_DIR}" && python main.py"',
    shell=True,
    env=os.environ
)

time.sleep(3)

# Launch Frontend
print("Starting Frontend...")
subprocess.Popen(
    f'start "Rice Frontend" cmd /k "cd /d "{FRONTEND_DIR}" && npm run dev"',
    shell=True,
    env=os.environ
)

print("Done! Check the two new terminal windows.")
