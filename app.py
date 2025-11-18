from db import load_json, save_json
import datetime
import csv
import os

CLUBES_FILE = os.path.join("data", "clubes.json")
INSCRICAO_DEADLINE = "2025-12-01"

def is_deadline_passed():
    deadline = datetime.datetime.fromisoformat(INSCRICAO_DEADLINE)
    return datetime.datetime.utcnow() > deadline

def submit_inscricao(user):
    if is_deadline_passed():
        print("As inscrições estão encerradas.")
        return
    clubes = load_json(CLUBES_FILE, [])
    nome_clube = input("Nome do clube: ").strip()
    for c in clubes:
        if c["nome"].lower() == nome_clube.lower():
            print("Erro: clube já inscrito.")
            return
    contacto = input("Contacto (email/tel): ").strip()
    cidade = input("Cidade: ").strip()
    clubes.append({
        "nome": nome_clube,
        "contacto": contacto,
        "cidade": cidade,
        "inscrito_por": user["username"],
        "time": datetime.datetime.utcnow().isoformat()+"Z"
    })
    save_json(CLUBES_FILE, clubes)
    print("Inscrição submetida com sucesso.")

def list_clubes():
    clubes = load_json(CLUBES_FILE, [])
    if not clubes:
        print("Nenhuma equipa inscrita.")
        return
    for i, c in enumerate(clubes, 1):
        print(f"{i}. {c['nome']} — {c.get('cidade','-')} — contacto: {c.get('contacto','-')} (inscrito por: {c.get('inscrito_por')})")

def export_clubes_csv():
    clubes = load_json(CLUBES_FILE, [])
    if not clubes:
        print("Nenhuma equipa para exportar.")
        return
    filename = os.path.join("data", f"equipas_export_{datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')}.csv")
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["nome","cidade","contacto","inscrito_por","time"])
        writer.writeheader()
        for c in clubes:
            writer.writerow(c)
    print(f"Exportado para {filename}")
