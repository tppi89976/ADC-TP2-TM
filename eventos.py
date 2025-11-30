import datetime
from db import carregar_json, guardar_json
from logs import registar_log

DATA_DIR = "data"
EVENTOS_FILE = f"{DATA_DIR}/eventos.json"

def listar_eventos():
    """
Lista todos os eventos registados no ficheiro de eventos.
Se não houver eventos, informa o utilizador.
"""
eventos = carregar_json(EVENTOS_FILE)
if not eventos:
    print("Nenhum evento registado.")



print("=== Eventos ===")
for i, e in enumerate(eventos, 1):
    print(f"{i}. {e.get('nome')} - data: {e.get('data')} - clube: {e.get('clube')}")
    
    eventos =listar_eventos()
    from db import guardar_json, EVENTOS_FILE
    guardar_json(EVENTOS_FILE, eventos)


def criar_evento():
    """
Cria um novo evento e guarda no ficheiro JSON.

```
:param user: Dicionário com informação do utilizador que cria o evento.
"""
if __name__ == "__main__":
    
    eventos = criar_evento()
    from db import guardar_json, EVENTOS_FILE
    guardar_json(EVENTOS_FILE, eventos)

   

eventos = carregar_json(EVENTOS_FILE)
nome = input("Nome do evento: ").strip()
data = input("Data do evento (YYYY-MM-DD): ").strip()
clube = input("Clube organizador: ").strip()

entry = {
    "nome": nome,
    "data": data,
    "clube": clube,
    "criado_por": ("username"),
    "time": datetime.datetime.utcnow().isoformat() + "Z"
}

eventos.append(entry)
guardar_json(EVENTOS_FILE, eventos)
registar_log(("username"), f"evento_criado:{nome}")
print("Evento criado com sucesso.")


def remover_evento(user):
    """
Remove um evento existente com base no índice apresentado na listagem.

```
:param user: Dicionário com informação do utilizador que remove o evento.
"""
    if user is None:
        print("Autenticação necessária.")
    return

eventos = carregar_json(EVENTOS_FILE)
listar_eventos()
try:
    idx = int(input("Número do evento a remover: "))
except ValueError:
    print("Número inválido.")
    

if 1 <= idx <= len(eventos):
    ev = eventos.pop(idx - 1)
    guardar_json(EVENTOS_FILE, eventos)
    registar_log(("username"), f"evento_removido:{ev.get('nome')}")
    print(f"Evento {ev.get('nome')} removido com sucesso.")
else:
    print("Índice inválido.")


def buscar_evento():
    """
Pesquisa eventos pelo nome e mostra os resultados encontrados.
"""
eventos = carregar_json(EVENTOS_FILE)
termo = input("Buscar evento por nome: ").strip().lower()
encontrados = [e for e in eventos if termo in e.get("nome", "").lower()]


if not encontrados:
    print("Nenhum evento encontrado.")
    

print("=== Eventos Encontrados ===")
for e in encontrados:
    print(f"{e.get('nome')} - data: {e.get('data')} - clube: {e.get('clube')}")


def editar_evento():
    """
Permite editar os detalhes de um evento existente.

```
:param user: Dicionário com informação do utilizador que edita o evento.
"""

    

eventos = carregar_json(EVENTOS_FILE)
listar_eventos()
try:
    idx = int(input("Número do evento a editar: "))
except ValueError:
    print("Número inválido.")
   

if 1 <= idx <= len(eventos):
    ev = eventos[idx - 1]
    print(f"Editando {ev.get('nome')}")
    ev["nome"] = input(f"Novo nome [{ev.get('nome')}]: ").strip() or ev.get("nome")
    ev["data"] = input(f"Nova data [{ev.get('data')}]: ").strip() or ev.get("data")
    ev["clube"] = input(f"Novo clube [{ev.get('clube')}]: ").strip() or ev.get("clube")
    guardar_json(EVENTOS_FILE, eventos)
    registar_log(("username"), f"evento_editado:{ev.get('nome')}")
    print("Evento editado com sucesso.")
else:
    print("Índice inválido.")


def gerar_relatorio_eventos():
    """
Gera um relatório completo de todos os eventos registados.
"""
eventos = carregar_json(EVENTOS_FILE)
if not eventos:
    print("Nenhum evento registado.")
    


print("=== Relatório de Eventos ===")
for e in eventos:
    print(f"{e.get('nome')} - {e.get('data')} - Clube: {e.get('clube')} - Criado por: {e.get('criado_por')}")


if __name__ == "__main__":
    # Apenas roda interativamente quando chamado diretamente
    user = {"username": "teste"}
    listar_eventos()
