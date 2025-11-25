from db import carregar_json, guardar_json
from logs import registar_log
from utils import now_iso, CLUBES_FILE

def listar_clubes():
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