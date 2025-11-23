import json
import os
import hashlib
import datetime

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")


# --------------------
# Funções utilitárias
# --------------------

def now_iso():
    """Devolve a hora atual em formato ISO UTC."""
    return datetime.datetime.utcnow().isoformat() + "Z"


def load_json(path, default):
    """Carrega JSON. Se não existir devolve o default."""
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def save_json(path, data):
    """Guarda dados em JSON com indentação."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def hash_password(password: str) -> str:
    """Gera hash SHA256 para uma password."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


# -------------------------
# Gestão de utilizadores
# -------------------------

def get_user(username: str):
    """Procura e devolve um utilizador pelo username."""
    users = load_json(USERS_FILE, [])
    for u in users:
        if u["username"] == username:
            return u
    return None


def create_user(username: str, name: str, email: str, password: str, role="utilizador"):
    """Cria um novo utilizador e guarda no ficheiro."""
    users = load_json(USERS_FILE, [])

    # Verificar duplicado
    if any(u["username"] == username for u in users):
        return False, "Username já existe."

    entry = {
        "username": username,
        "name": name,
        "email": email,
        "role": role,
        "password_hash": hash_password(password),
        "created": now_iso()
    }

    users.append(entry)
    save_json(USERS_FILE, users)
    return True, "Utilizador criado com sucesso."


def authenticate(username: str, password: str):
    """
    Verifica se o utilizador existe e valida a password.
    Devolve:
    - user dict (se ok)
    - None (se falhar)
    """
    user = get_user(username)
    if not user:
        return None

    if user["password_hash"] != hash_password(password):
        return None

    return user


def change_password(username: str, new_password: str):
    """Altera password de um utilizador existente."""
    users = load_json(USERS_FILE, [])
    for u in users:
        if u["username"] == username:
            u["password_hash"] = hash_password(new_password)
            save_json(USERS_FILE, users)
            return True, "Password atualizada."

    return False, "Utilizador não encontrado."
