import json
import os

EVENTOS_FILE = "data/eventos.json"
def carregar_json(file_path):
    """
    Carrega dados de um ficheiro JSON.

    :param file_path: Caminho do ficheiro JSON a carregar.
    :type file_path: str
    :return: Conteúdo do ficheiro JSON como lista ou dicionário. Se o ficheiro não existir, retorna lista vazia.
    :rtype: list | dict
    :raises json.JSONDecodeError: Se o ficheiro não contiver JSON válido.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        raise


def guardar_json(file_path, dados):
    """
    Guarda dados em formato JSON num ficheiro, criando a pasta se necessário.

    :param file_path: Caminho do ficheiro JSON a criar ou sobrescrever.
    :type file_path: str
    :param dados: Dados a guardar (lista ou dicionário).
    :type dados: list | dict
    :return: None
    :rtype: None
    """
    # Garante que a pasta exista
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

