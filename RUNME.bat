IF EXIST ".venv" (
    call .venv\Scripts\activate
    call cmd /k "C:\Users\sieve\OneDrive\Desktop\Coding\Projects\PC-Logger\src\protector.ps1"
    start /B cmd /k "C:\Users\sieve\OneDrive\Desktop\Coding\Projects\PC-Logger\.venv\Scripts\python.exe C:\Users\sieve\OneDrive\Desktop\Coding\Projects\PC-Logger\src\main_sender.py"
) ELSE (
    python -m venv .venv
    call .venv\Scripts\activate
    pip install -r requirements.txt
)