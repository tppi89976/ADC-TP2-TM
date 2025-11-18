import os
import json

def load_json(path, default=None):
    """
    Carrega dados de um ficheiro JSON.
    
    Args:
        path (str): caminho do ficheiro
        default: valor retornado caso o ficheiro não exista ou esteja vazio
    Returns:
        dict/list: dados carregados do JSON ou default
    """
    if not os.path.exists(path):
        return default if default is not None else []
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except Exception:
            return default if default is not None else []

def save_json(path, data):
    """
    Guarda dados num ficheiro JSON.
    
    Args:
        path (str): caminho do ficheiro
        data (dict/list): dados a guardar
    """
    dir_name = os.path.dirname(path)
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
