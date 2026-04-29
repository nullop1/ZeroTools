@echo off
echo If your internet is restricted, consider using a mirror: runflare.com/mirrors
echo Upgrading Python PIP...
python -m pip install --upgrade pip
echo Installing Python libraries from requirements.txt...
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo Failed to install some libraries.
    echo Try using a mirror: runflare.com/mirrors
    pause
    exit /b
)

echo Libraries installed successfully!
echo Running main.py...
python main.py
pause
