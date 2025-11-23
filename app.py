#!/usr/bin/env python3
"""
app.py - Integração das features do TP2 (passo-a-passo)
"""

# imports dos módulos de feature (devem existir nos ficheiros correspondentes)
from db import carregar_json, guardar_json
from logs import registar_log
from admin import listar_inscricoes_admin
from permissoes import verificar_role
from auth import register_user, authenticate, change_password

DATA_DIR = "data"
CLUBES_FILE = f"{DATA_DIR}/clubes.json"
