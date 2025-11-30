"""
Módulo de gestão de clubes.

Este módulo permite listar, submeter, remover e editar clubes.
Inclui funções de logging para cada operação.
"""
from db import carregar_json, guardar_json
from logs import registar_log

from utils import now_iso, CLUBES_FILE

# db.py
def carregar_json(filename):
    """Stub para autodoc"""
    return []

def guardar_json(filename, data):
    """Stub para autodoc"""
    pass

# utils.py
CLUBES_FILE = "clubes.json"
USERS_FILE = "users.json"
LOGS_FILE = "logs.json"

from datetime import datetime
def now_iso():
    return datetime.now().isoformat()



def listar_clubes():
    """
    Lista todos os clubes registados.

    Mostra o nome, cidade e contacto de cada clube.
    """
    clubes = carregar_json(CLUBES_FILE)
    if not clubes:
        print("Nenhuma equipa inscrita.")
        return
    print("=== Equipas Inscritas ===")
    for i, c in enumerate(clubes, 1):
        print(f"{i}. {c.get('nome')} — {c.get('cidade','-')} — contacto: {c.get('contacto','-')} (inscrito por: {c.get('inscrito_por')})")


def submeter_clube(user):
    
    if user is None:
        print("Tem de estar autenticado para submeter inscrições.")
        return
    clubes = carregar_json(CLUBES_FILE)
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
    
    """
    Submete um novo clube.

    Apenas utilizadores autenticados podem submeter.
    Verifica duplicações e regista log.
    """
def remover_clube(user):
  
    clubes = carregar_json(CLUBES_FILE)
    nome = input("Nome do clube a remover: ").strip()
    clube = next((c for c in clubes if c['nome'].lower() == nome.lower()), None)
    if not clube:
        print("Clube não encontrado.")
        return
    if user['role'] != 'administrador' and clube['inscrito_por'] != user['username']:
        print("Não tens permissão para remover este clube.")
        return
    clubes.remove(clube)
    guardar_json(CLUBES_FILE, clubes)
    print(f"Clube {nome} removido com sucesso.")

    """
    Remove um clube existente.

    Apenas o administrador ou quem submeteu pode remover.
    """

def editar_clube(user):
    clubes = carregar_json(CLUBES_FILE)
    nome = input("Nome do clube a editar: ").strip()
    clube = next((c for c in clubes if c['nome'].lower() == nome.lower()), None)
    if not clube:
        print("Clube não encontrado.")
        return
    if user['role'] != 'administrador' and clube['inscrito_por'] != user['username']:
        print("Não tens permissão para editar este clube.")
        return
    novo_nome = input(f"Novo nome ({clube['nome']}): ").strip() or clube['nome']
    novo_contato = input(f"Novo contacto ({clube.get('contacto','-')}): ").strip() or clube.get('contacto','-')
    nova_cidade = input(f"Nova cidade ({clube.get('cidade','-')}): ").strip() or clube.get('cidade','-')
    clube.update({"nome": novo_nome, "contacto": novo_contato, "cidade": nova_cidade})
    guardar_json(CLUBES_FILE, clubes)
    print("Clube atualizado com sucesso.")

    """
    Edita informações de um clube existente.

    Apenas o administrador ou quem submeteu pode editar.
    """
