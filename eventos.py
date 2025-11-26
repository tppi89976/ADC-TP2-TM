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

    def remover_evento(user):
        if user is None:
            print("Autenticação necessária.")
        return
    eventos = carregar_json(EVENTOS_FILE)
    listar_eventos()
    idx = int(input("Número do evento a remover: "))
    if 1 <= idx <= len(eventos):
        ev = eventos.pop(idx-1)
        guardar_json(EVENTOS_FILE, eventos)
        registar_log(user.get("username"), f"evento_removido:{ev.get('nome')}")
        print(f"Evento {ev.get('nome')} removido com sucesso.")
    else:
        print("Índice inválido.")
    
def buscar_evento():
    eventos = carregar_json(EVENTOS_FILE)
    termo = input("Buscar evento por nome: ").strip().lower()
    encontrados = [e for e in eventos if termo in e.get("nome","").lower()]
    if not encontrados:
        print("Nenhum evento encontrado.")
        return
    print("=== Eventos Encontrados ===")
    for e in encontrados:
        print(f"{e.get('nome')} - data: {e.get('data')} - clube: {e.get('clube')}")

def editar_evento(user):
    if user is None:
        print("Autenticação necessária.")
        return
    eventos = carregar_json(EVENTOS_FILE)
    listar_eventos()
    idx = int(input("Número do evento a editar: "))
    if 1 <= idx <= len(eventos):
        ev = eventos[idx-1]
        print(f"Editando {ev.get('nome')}")
        ev["nome"] = input(f"Novo nome [{ev.get('nome')}]: ").strip() or ev.get("nome")
        ev["data"] = input(f"Nova data [{ev.get('data')}]: ").strip() or ev.get("data")
        ev["clube"] = input(f"Novo clube [{ev.get('clube')}]: ").strip() or ev.get("clube")
        guardar_json(EVENTOS_FILE, eventos)
        registar_log(user.get("username"), f"evento_editado:{ev.get('nome')}")
        print("Evento editado com sucesso.")
    else:
        print("Índice inválido.")