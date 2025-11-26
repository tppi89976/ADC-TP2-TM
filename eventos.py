# eventos.py
import datetime
from db import carregar_json, guardar_json
from logs import registar_log

DATA_DIR = "data"
EVENTOS_FILE = f"{DATA_DIR}/eventos.json"

def listar_eventos():
    eventos = carregar_json(EVENTOS_FILE)
    if not eventos:
        print("Nenhum evento registado.")
        return
    print("=== Eventos ===")
    for i, e in enumerate(eventos, 1):
        print(f"{i}. {e.get('nome')} - data: {e.get('data')} - clube: {e.get('clube')}")

def criar_evento(user):
    if user is None:
        print("Autenticação necessária.")
        return
    eventos = carregar_json(EVENTOS_FILE)
    nome = input("Nome do evento: ").strip()
    data = input("Data do evento (YYYY-MM-DD): ").strip()
    clube = input("Clube organizador: ").strip()
    entry = {
        "nome": nome,
        "data": data,
        "clube": clube,
        "criado_por": user.get("username"),
        "time": datetime.datetime.utcnow().isoformat()+"Z"
    }
    eventos.append(entry)
    guardar_json(EVENTOS_FILE, eventos)
    registar_log(user.get("username"), f"evento_criado:{nome}")
    print("Evento criado com sucesso.")