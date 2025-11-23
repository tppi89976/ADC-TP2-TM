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
