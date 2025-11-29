#!/usr/bin/env python3
import os
import datetime
"""
app.py - Integração das features do TP2 (passo-a-passo)
"""

from db import carregar_json, guardar_json
from logs import registar_log
from admin import listar_inscricoes_admin
from permissoes import verificar_role
from auth import register_user, authenticate, change_password
from clubes import listar_clubes, submeter_clube, remover_clube, editar_clube
from eventos import listar_eventos, criar_evento, remover_evento, editar_evento, gerar_relatorio_eventos
from profile import view_profile, update_name, update_email, update_phone, change_password, delete_account, update_preferences

DATA_DIR = "data"
CLUBES_FILE = f"{DATA_DIR}/clubes.json"
USERS_FILE = f"{DATA_DIR}/users.json"
EVENTOS_FILE = f"{DATA_DIR}/eventos.json"

def ensure_data_files():
    """Garante que os ficheiros JSON existem"""
    os.makedirs(DATA_DIR, exist_ok=True)
    for f in [USERS_FILE, CLUBES_FILE, EVENTOS_FILE, f"{DATA_DIR}/logs.json"]:
        if not os.path.exists(f):
            guardar_json(f, [])

def now_iso():
    return datetime.datetime.utcnow().isoformat() + "Z"

def authenticate_user():
    from auth import authenticate
    username = input("Username: ").strip()
    pwd = input("Password: ").strip()
    user = authenticate(username, pwd)
    if user:
        print(f"Bem-vindo, {user.get('name', username)} ({user.get('role')})")
        registar_log(username, "login")
        return user
    print("Falha na autenticação.")
    registar_log(username, "login_failed")
    return None


def menu_anonymous():
    while True:
        print("\n--- Menu Principal ---")
        print("1) Registar")
        print("2) Login")
        print("0) Sair")
        choice = input("> ").strip()
        if choice == "1":
            from auth import register_user
            register_user()
        elif choice == "2":
            user = authenticate_user()
            if user:
                menu_user(user)
        elif choice == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")



def menu_user(user):
    while True:
        print(f"\n--- Menu ({user.get('username')} - {user.get('role')}) ---")
        print("1) Ver perfil")
        print("2) Atualizar nome")
        print("3) Atualizar email")
        print("4) Atualizar telefone")
        print("5) Alterar password")
        print("6) Atualizar preferências")
        print("7) Eliminar conta")
        print("8) Listar clubes")
        print("9) Submeter clube")
        print("10) Editar clube")
        print("11) Remover clube")
        print("12) Listar eventos")
        print("13) Criar evento")
        print("14) Editar evento")
        print("15) Remover evento")
        print("16) Relatório de eventos")
        print("0) Logout")
        choice = input("> ").strip()
        if choice == "1":
            # se tiveres uma função update_profile em auth.py, chama-a
            try:
                from auth import update_profile
                update_profile(user)
            except Exception:
                print("Funcionalidade update_profile indisponível.")
        elif choice == "2":
            change_password(user)
        elif choice == "3":
            print("Eliminar conta: usar auth.delete_account se existir.")
        elif choice == "4":
            submeter_clube(user)
        elif choice == "5":
            listar_clubes()
        elif choice == "6" and verificar_role(user, "administrador"):
            listar_inscricoes_admin()
        elif choice == "9":
            registar_log(user.get("username"), "logout")
            break
        else:
            print("Opção inválida.")
# -------------------------
# Entry point
# -------------------------
def main():
    bootstrap_files()
    menu_anonymous()

if __name__ == "__main__":
    main()
