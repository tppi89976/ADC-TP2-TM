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

DATA_DIR = "data"
CLUBES_FILE = f"{DATA_DIR}/clubes.json"

def ensure_data_dir():
    if not os.path.isdir(DATA_DIR):
        os.makedirs(DATA_DIR)

def now_iso():
    return datetime.datetime.utcnow().isoformat() + "Z"

def bootstrap_files():
    """
    Garante que os ficheiros JSON existem (criando vazios se necessário).
    """
    ensure_data_dir()
    # criar ficheiros vazios se não existirem
    for p in (CLUBES_FILE, f"{DATA_DIR}/users.json", f"{DATA_DIR}/logs.json"):
        if not os.path.exists(p):
            guardar_json(p, [])  # usa a função de db.py

# -------------------------
# Clubes (leitura)
# -------------------------
def listar_clubes():
    clubes = carregar_json(CLUBES_FILE)
    if not clubes:
        print("Nenhuma equipa inscrita.")
        return
    print("=== Equipas Inscritas ===")
    for i, c in enumerate(clubes, 1):
        print(f"{i}. {c.get('nome')} — {c.get('cidade','-')} — contacto: {c.get('contacto','-')} (inscrito por: {c.get('inscrito_por')})")
# -------------------------
# Clubes (escrita)
# -------------------------
def submeter_clube(user):
    if user is None:
        print("Tem de estar autenticado para submeter inscrições.")
        return
    clubes = carregar_json(CLUBES_FILE)
    print("=== Submeter Inscrição de Clube ===")
    nome = input("Nome do clube: ").strip()
    if any(c.get("nome","").lower() == nome.lower() for c in clubes):
        print("Erro: clube já inscrito.")
        registar_log(user.get("username","anon"), f"inscricao_duplicada:{nome}")
        return
    contacto = input("Contacto (email/tel): ").strip()
    cidade = input("Cidade: ").strip()
    entry = {
        "nome": nome,
        "contacto": contacto,
        "cidade": cidade,
        "inscrito_por": user.get("username"),
        "time": now_iso()
    }
    clubes.append(entry)
    guardar_json(CLUBES_FILE, clubes)
    registar_log(user.get("username"), f"inscricao_submetida:{nome}")
    print("Inscrição submetida com sucesso.")
# -------------------------
# Autenticação & menus
# -------------------------
def menu_anonymous():
    while True:
        print("\n--- Menu Principal ---")
        print("1) Registar")
        print("2) Login")
        print("0) Sair")
        c = input("> ").strip()
        if c == "1":
            register_user()   # função do auth.py
        elif c == "2":
            user = login_flow()
            if user:
                menu_user(user)
        elif c == "0":
            print("Até logo.")
            break
        else:
            print("Opção inválida.")

def login_flow():
    print("=== Login ===")
    username = input("username: ").strip()
    pwd = input("Password: ").strip()
    user = authenticate(username, pwd)
    if not user:
        print("Autenticação falhou.")
        registar_log("anon", f"login_failed:{username}")
        return None
    print(f"Bem-vindo, {user.get('name',username)} ({user.get('role')})")
    registar_log(user.get("username"), "login")
    return user

def menu_user(user):
    role = user.get("role")
    while True:
        print(f"\n--- Menu ({user.get('username')} - {role}) ---")
        print("1) Atualizar dados pessoais (via auth module)")
        print("2) Alterar password")
        print("3) Eliminar conta (não implementado aqui)")
        print("4) Submeter inscrição de clube")
        print("5) Ver clubes")
        if verificar_role(user, "administrador"):
            print("6) Painel administrador (listar inscrições + logs)")
        print("9) Logout")
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
