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
