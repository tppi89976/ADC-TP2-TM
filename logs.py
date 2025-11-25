import datetime
from db import load_json, save_json

LOGS_FILE = "data/logs.json"

def now_iso():
    return datetime.datetime.utcnow().isoformat() + "Z"

def log_action(actor, action, details=""):
    logs = load_json(LOGS_FILE, [])
    entry = {
        "time": now_iso(),
        "actor": actor,
        "action": action,
        "details": details
    }
    logs.append(entry)
    save_json(LOGS_FILE, logs)
