from constants import LOG_FILE

def load_logs(file_path=LOG_FILE):
    with open(file_path, "r") as f:
        logs = f.readlines()
    return [log.strip() for log in logs]

def filter_logs(logs, keyword):
    """Return logs containing the keyword"""
    return [log for log in logs if keyword.lower() in log.lower()]
