import json
import datetime
import os

LOGS_FILE = os.path.join("data", "logs.json")

def now_iso():
    return datetime.datetime.utcnow().isoformat() + "Z"

def registar_log(actor, acao, detalhes=""):
    if not os.path.exists("data"):
        os.makedirs("data")
    logs = []
    if os.path.exists(LOGS_FILE):
        with open(LOGS_FILE, "r", encoding="utf-8") as f:
            try:
                logs = json.load(f)
            except:
                logs = []
    logs.append({
        "time": now_iso(),
        "actor": actor,
        "action": acao,
        "details": detalhes
    })
    with open(LOGS_FILE, "w", encoding="utf-8") as f:

        json.dump(logs, f, indent=2, ensure_ascii=False)