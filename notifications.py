import os
import json

DATA_DIR = "data"
NOTIFICACOES_FILE = f"{DATA_DIR}/notificacoes.json"
def ensure_notificacoes_file():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(NOTIFICACOES_FILE):
        with open(NOTIFICACOES_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)
