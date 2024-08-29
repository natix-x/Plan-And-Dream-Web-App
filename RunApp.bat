@echo off

:: Check if the virtual environment is already activated
if not defined VIRTUAL_ENV (
    echo Activating virtual environment...
    call VenvSetup.bat
)

echo Initializing...
call python run.py