IF EXIST ".venv" (
    call .venv\Scripts\activate
    call powershell -ExecutionPolicy Bypass -File "src\protector.ps1"
    start /B cmd /k "python.exe src\main_sender.py"
) ELSE (
    python -m venv .venv
    call .venv\Scripts\activate
    pip install -r requirements.txt
)