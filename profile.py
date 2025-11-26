
import datetime
from db import carregar_json, guardar_json
from logs import registar_log

USERS_FILE = "data/users.json"

def now_iso():
    return datetime.datetime.utcnow().isoformat() + "Z"

# -------------------------
# Visualizar perfil
# -------------------------
def view_profile(user):
    print("\n=== Perfil do Usuário ===")
    print(f"Username: {user.get('username')}")
    print(f"Nome: {user.get('name', '-')}")
    print(f"Email: {user.get('email', '-')}")
    print(f"Telefone: {user.get('phone', '-')}")
    print(f"Preferências: {user.get('preferences', {})}")
    print(f"Role: {user.get('role', '-')}")
    print("=========================")

