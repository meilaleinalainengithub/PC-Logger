IF EXIST ".venv" (
    python "\src\main_sender.py"
    timeout /t  3 /nobreak
    python "\src\screen_sender.py"
    python "\src\mic_sender.py"
) ELSE (
    python -m venv .venv
    call .venv\Scripts\activate
    pip install -r requirements.txt
)