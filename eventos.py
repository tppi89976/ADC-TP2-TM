import datetime
from db import carregar_json, guardar_json, EVENTOS_FILE
from logs import registar_log

DATA_DIR = "data"
EVENTOS_FILE = f"{DATA_DIR}/eventos.json"


def listar_eventos():
    """
    Lista todos os eventos registados no ficheiro de eventos.

    :return: Lista de eventos (pode estar vazia)
    """
    eventos = carregar_json(EVENTOS_FILE) or []
    return eventos


def criar_evento(nome, data, clube, username):
    """
    Cria um novo evento e guarda no ficheiro JSON.

    :param nome: Nome do evento
    :param data: Data do evento (YYYY-MM-DD)
    :param clube: Clube organizador
    :param username: Username do utilizador que cria o evento
    :return: Evento criado
    """
    eventos = carregar_json(EVENTOS_FILE) or []

    entry = {
        "nome": nome,
        "data": data,
        "clube": clube,
        "criado_por": username,
        "time": datetime.datetime.utcnow().isoformat() + "Z"
    }

    eventos.append(entry)
    guardar_json(EVENTOS_FILE, eventos)
    registar_log(username, f"evento_criado:{nome}")
    return entry


def remover_evento(idx, username):
    """
    Remove um evento pelo índice da lista.

    :param idx: Índice do evento a remover (1-based)
    :param username: Username do utilizador que remove o evento
    :return: Evento removido ou None
    """
    eventos = carregar_json(EVENTOS_FILE) or []

    if 1 <= idx <= len(eventos):
        ev = eventos.pop(idx - 1)
        guardar_json(EVENTOS_FILE, eventos)
        registar_log(username, f"evento_removido:{ev.get('nome')}")
        return ev
    return None


def buscar_evento(termo):
    """
    Pesquisa eventos pelo nome.

    :param termo: Termo de pesquisa (string)
    :return: Lista de eventos encontrados
    """
    eventos = carregar_json(EVENTOS_FILE) or []
    encontrados = [e for e in eventos if termo.lower() in e.get("nome", "").lower()]
    return encontrados


def editar_evento(idx, nome=None, data=None, clube=None, username=None):
    """
    Edita os detalhes de um evento existente.

    :param idx: Índice do evento a editar (1-based)
    :param nome: Novo nome (opcional)
    :param data: Nova data (opcional)
    :param clube: Novo clube (opcional)
    :param username: Username do utilizador que edita
    :return: Evento editado ou None
    """
    eventos = carregar_json(EVENTOS_FILE) or []

    if 1 <= idx <= len(eventos):
        ev = eventos[idx - 1]
        ev["nome"] = nome or ev.get("nome")
        ev["data"] = data or ev.get("data")
        ev["clube"] = clube or ev.get("clube")
        guardar_json(EVENTOS_FILE, eventos)
        if username:
            registar_log(username, f"evento_editado:{ev.get('nome')}")
        return ev
    return None


def gerar_relatorio_eventos():
    """
    Gera relatório completo de todos os eventos registados.

    :return: Lista de eventos
    """
    eventos = carregar_json(EVENTOS_FILE) or []
    return eventos


if __name__ == "__main__":
    # Código interativo para testes
    eventos = listar_eventos()
    print("=== Eventos ===")
    for i, e in enumerate(eventos, 1):
        print(f"{i}. {e.get('nome')} - {e.get('data')} - Clube: {e.get('clube')}")
