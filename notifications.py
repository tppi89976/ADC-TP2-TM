import os
import json
import datetime

DATA_DIR = "data"
NOTIFICACOES_FILE = f"{DATA_DIR}/notificacoes.json"
def ensure_notificacoes_file():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(NOTIFICACOES_FILE):
        with open(NOTIFICACOES_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)

def salvar_notificacao(usuario, mensagem):
    """Salva uma notificação para um usuário"""
    ensure_notificacoes_file()
    with open(NOTIFICACOES_FILE, "r", encoding="utf-8") as f:
        notificacoes = json.load(f)
    
    entry = {
        "usuario": usuario.get("username"),
        "mensagem": mensagem,
        "time": datetime.datetime.utcnow().isoformat() + "Z"
    }
    notificacoes.append(entry)
    with open(NOTIFICACOES_FILE, "w", encoding="utf-8") as f:
        json.dump(notificacoes, f, indent=4)

def notificar_evento(usuario, evento, acao):
    """Notifica sobre ações em eventos"""
    msg = f"Evento '{evento.get('nome')}' foi {acao}."
    print(msg)
    salvar_notificacao(usuario, msg)


def notificar_novo_usuario(usuario):
    """Notifica sobre registro de novo usuário"""
    msg = f"Novo usuário registrado: {usuario.get('username')}"
    print(msg)
    salvar_notificacao(usuario, msg)

def notificar_preferencia(usuario, pref, valor):
    """Notifica sobre alteração de preferência"""
    msg = f"Sua preferência '{pref}' foi alterada para '{valor}'"
    print(msg)
    salvar_notificacao(usuario, msg)

def listar_notificacoes(usuario):
    """Lista todas as notificações de um usuário"""
    ensure_notificacoes_file()
    with open(NOTIFICACOES_FILE, "r", encoding="utf-8") as f:
        notificacoes = json.load(f)
    
    user_notifs = [n for n in notificacoes if n["usuario"] == usuario.get("username")]
    if not user_notifs:
        print("Nenhuma notificação encontrada.")
        return
    
    print(f"=== Notificações de {usuario.get('username')} ===")
    for n in user_notifs:
        print(f"- {n['mensagem']} ({n['time']})")