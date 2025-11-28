
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


def update_name(user):
    new_name = input("Novo nome: ").strip()
    if new_name:
        user['name'] = new_name
        save_user(user)
        registar_log(user['username'], f"update_name:{new_name}")
        print("Nome atualizado com sucesso.")


def update_email(user):
    new_email = input("Novo email: ").strip()
    if new_email:
        user['email'] = new_email
        save_user(user)
        registar_log(user['username'], f"update_email:{new_email}")
        print("Email atualizado com sucesso.")


def update_phone(user):
    new_phone = input("Novo telefone: ").strip()
    if new_phone:
        user['phone'] = new_phone
        save_user(user)
        registar_log(user['username'], f"update_phone:{new_phone}")
        print("Telefone atualizado com sucesso.")

def change_password(user):
    from auth import authenticate  # reutiliza função existente
    old_pwd = input("Password atual: ").strip()
    if authenticate(user['username'], old_pwd):
        new_pwd = input("Nova password: ").strip()
        confirm_pwd = input("Confirmar nova password: ").strip()
        if new_pwd == confirm_pwd and new_pwd:
            user['password'] = new_pwd
            save_user(user)
            registar_log(user['username'], "password_changed")
            print("Password alterada com sucesso.")
        else:
            print("Senhas não coincidem ou inválida.")
    else:
        print("Password atual incorreta.")

def delete_account(user):
    confirmation = input(f"Tem a certeza que quer eliminar a conta {user['username']}? (s/n) ").strip().lower()
    if confirmation == 's':
        users = carregar_json(USERS_FILE)
        users = [u for u in users if u['username'] != user['username']]
        guardar_json(USERS_FILE, users)
        registar_log(user['username'], "account_deleted")
        print("Conta eliminada com sucesso.")
        return True
    print("Operação cancelada.")
    return False


def update_preferences(user):
    prefs = user.get('preferences', {})
    print("\n=== Preferências atuais ===")
    for k, v in prefs.items():
        print(f"{k}: {v}")
    key = input("Qual preferência deseja alterar? (ex: notificacao, tema) ").strip()
    value = input("Novo valor: ").strip()
    if key and value:
        prefs[key] = value
        user['preferences'] = prefs
        save_user(user)
        registar_log(user['username'], f"preference_updated:{key}={value}")
        print("Preferência atualizada com sucesso.")

def activity_log(user):
    print(f"\n=== Histórico de atividades ({user['username']}) ===")
    logs = carregar_json("data/logs.json")
    user_logs = [l for l in logs if l.get('user') == user['username']]
    if not user_logs:
        print("Sem atividades registradas.")
        return
    for l in user_logs:
        print(f"{l.get('time')} - {l.get('action')}")
    print("==============================")


