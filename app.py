#!/usr/bin/env python3
import os
import datetime
"""
app.py - Integração das features do TP2 (passo-a-passo)

Este módulo centraliza todas as funcionalidades do sistema:

Gestão de usuários (perfil, autenticação, registro)

Gestão de clubes (listar, submeter, editar, remover)

Gestão de eventos (listar, criar, editar, remover, gerar relatório)

Logging de ações dos usuários

Arquivos de dados usados:

data/users.json

data/clubes.json

data/eventos.json

data/logs.json

Dependências:

db.py : funções de carregamento e gravação JSON

logs.py : função registar_log()

auth.py : autenticação e registro de usuários

clubes.py : funções CRUD de clubes

eventos.py : funções CRUD de eventos

profile.py : funções de perfil de usuário
"""

from db import carregar_json, guardar_json
from logs import registar_log

from clubes import listar_clubes, submeter_clube, remover_clube, editar_clube
from eventos import listar_eventos, criar_evento, remover_evento, editar_evento, gerar_relatorio_eventos, buscar_evento
from profile import view_profile, update_name, update_email, update_phone, change_password, delete_account, update_preferences

DATA_DIR = "data"
CLUBES_FILE = f"{DATA_DIR}/clubes.json"
USERS_FILE = f"{DATA_DIR}/users.json"
EVENTOS_FILE = f"{DATA_DIR}/eventos.json"

def ensure_data_files():
    """Garante que os ficheiros de dados existem"""
    """Garante que os ficheiros JSON existem"""
    os.makedirs(DATA_DIR, exist_ok=True)
    for f in [USERS_FILE, CLUBES_FILE, EVENTOS_FILE, f"{DATA_DIR}/logs.json"]:
        if not os.path.exists(f):
            guardar_json(f, [])

def now_iso():
    """
Retorna a data e hora atual em formato ISO 8601 UTC.

:return: str, data/hora no formato ISO 8601
"""
    return datetime.datetime.utcnow().isoformat() + "Z"

def authenticate_user():
    """
Solicita username e senha do usuário e tenta autenticar.
Registra login ou falha no log.

:return: dict do usuário autenticado ou None se falhar
"""
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
    """
Menu inicial para usuários não autenticados.
Permite registrar-se, fazer login ou sair.
"""
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
    """
Menu principal para usuários autenticados.
Permite acessar todas as funcionalidades do sistema.

:param user: dict contendo informações do usuário logado
"""
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
            view_profile(user)
        elif choice == "2":
            update_name(user)
        elif choice == "3":
            update_email(user)
        elif choice == "4":
            update_phone(user)
        elif choice == "5":
            change_password(user)
        elif choice == "6":
            update_preferences(user)
        elif choice == "7":
            if delete_account(user):
                break
        elif choice == "8":
            listar_clubes()
        elif choice == "9":
            submeter_clube(user)
        elif choice == "10":
            editar_clube(user)
        elif choice == "11":
            remover_clube(user)
        elif choice == "12":
            listar_eventos()
        elif choice == "13":
            criar_evento(user)
        elif choice == "14":
            editar_evento(user)
        elif choice == "15":
            remover_evento(user)
        elif choice == "16":
            gerar_relatorio_eventos()
        elif choice == "0":
            registar_log(user.get("username"), "logout")
            break
        else:
            print("Opção inválida.")
def main():
    ensure_data_files()
    menu_anonymous()

if __name__ == "__main__":
    main()
