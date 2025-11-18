import json

ligas_abertas = True
inscricoes_pendentes = []
jogadores_confirmados = []
equipas = ["benfica", "Porto", "Sporting", "Braga", "Guimarães", "Boavista"]




def listar_equipas():
    """US-05 – P2 — Listar equipas disponíveis."""
    print("\nEquipas disponíveis:")
    for e in equipas:
        print(" -", e)
    print()


def criar_inscricao():
    """Criar inscrição de um utilizador (dependente do estado da liga)."""
    if not ligas_abertas:
        print("\n Inscrições bloqueadas pelo administrador.\n")
        return

    nome = input("Nome do jogador: ")
    idade = input("Idade: ")
    equipa = input("Equipa pretendida: ")

    inscricoes_pendentes.append({
        "nome": nome,
        "idade": idade,
        "equipa": equipa
    })

    print(f"\nInscrição pendente criada para {nome}.\n")


def validar_inscricao(nome):
    """US-01 – P3 — Validar inscrição pendente."""
    for jogador in inscricoes_pendentes:
        if jogador["nome"].lower() == nome.lower():
            jogadores_confirmados.append(jogador)
            inscricoes_pendentes.remove(jogador)
            print(f"\n✔ Jogador {nome} foi validado!\n")
            return

    print("\n Jogador não encontrado nas inscrições pendentes.\n")


def atualizar_inscricao(nome_atual, novo_nome=None, nova_idade=None):
    """US-06 – P3 — Atualizar inscrição ainda pendente."""
    for jogador in inscricoes_pendentes:
        if jogador["nome"].lower() == nome_atual.lower():
            if novo_nome:
                jogador["nome"] = novo_nome
            if nova_idade:
                jogador["idade"] = nova_idade

            print("\n✔ Inscrição atualizada:", jogador, "\n")
            return

    print("\n Jogador não encontrado.\n")


def gerar_relatorio():
    """US-02 – P5 — Relatório das equipas inscritas."""
    print("\n===== RELATÓRIO DA LIGA PORTUGUESA =====")
    if not jogadores_confirmados:
        print("Ainda não existem jogadores confirmados.")
    else:
        for j in jogadores_confirmados:
            print(f"{j['nome']} ({j['idade']} anos) -> {j['equipa']}")
    print("=========================================\n")


def bloquear_inscricoes():
    """US-03 – P8 — Bloquear inscrições."""
    global ligas_abertas
    ligas_abertas = False
    print("\n🔒 As inscrições foram bloqueadas.\n")


def desbloquear_inscricoes():
    """Função auxiliar extra."""
    global ligas_abertas
    ligas_abertas = True
    print("\n🔓 Inscrições desbloqueadas.\n")


def exportar_backup():
    """US-04 – P13 — Exportar dados para JSON."""
    dados = {
        "pendentes": inscricoes_pendentes,
        "confirmados": jogadores_confirmados,
        "equipas": equipas,
        "estado_inscricoes": "abertas" if ligas_abertas else "bloqueadas"
    }

    with open("backup_liga.json", "w") as f:
        json.dump(dados, f, indent=4)

    print("\n📁 Backup criado: backup_liga.json\n")


# ============================================================
# MENU PRINCIPAL (CLI)
# ============================================================

def menu():
    while True:
        print("====== LIGA PORTUGUESA - SISTEMA DE INSCRIÇÕES ======")
        print("1. Criar inscrição (utilizador)")
        print("2. Validar inscrição (gestor)")
        print("3. Atualizar inscrição (utilizador)")
        print("4. Listar equipas (utilizador)")
        print("5. Gerar relatório (gestor)")
        print("6. Bloquear inscrições (administrador)")
        print("7. Desbloquear inscrições (administrador)")
        print("8. Exportar backup JSON (administrador)")
        print("0. Sair")
        print("=====================================================")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            criar_inscricao()
        elif opc == "2":
            nome = input("Nome do jogador a validar: ")
            validar_inscricao(nome)
        elif opc == "3":
            nome_atual = input("Nome atual: ")
            novo_nome = input("Novo nome (ou Enter): ") or None
            idade = input("Nova idade (ou Enter): ")
            nova_idade = int(idade) if idade else None
            atualizar_inscricao(nome_atual, novo_nome, nova_idade)
        elif opc == "4":
            listar_equipas()
        elif opc == "5":
            gerar_relatorio()
        elif opc == "6":
            bloquear_inscricoes()
        elif opc == "7":
            desbloquear_inscricoes()
        elif opc == "8":
            exportar_backup()
        elif opc == "0":
            print("\nA sair do sistema...")
            break
        else:
            print("\nOpção inválida!\n")


# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == "__main__":
    menu()
