import os
from datetime import datetime

def initialize_logs(log_dir="logs", filename="key_failures.log"):
    """
    Ensures the log directory and file exist. Initializes with a symbolic header if absent.
    """
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, filename)

    if not os.path.exists(log_path):
        with open(log_path, "a") as f:
            f.write(f"🌀 Log initialized at {datetime.now().isoformat()}\n")

def log_error(message, log_dir="logs", filename="key_failures.log", archetype="⚠️"):
    """
    Appends an error message to the log file with optional symbolic archetype.
    """
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, filename)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a") as f:
        f.write(f"{archetype} [{timestamp}] {message}\n")
