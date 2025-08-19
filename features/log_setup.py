import os

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

with open(os.path.join(log_dir, "key_failures.log"), "a") as f:
    f.write("Log initialized\n")
