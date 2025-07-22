import random
import os
import time

# Lista global de funções do jogo
funcoes = ["Top laner", "Jungler", "Mid laner", "Atirador", "Suporte"]

def animacao_loading():
    """Exibe uma animação de contagem regressiva para criar suspense."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Sorteio realizado. Preparando para revelar os times...")
    time.sleep(1.5)
    
    for i in range(3, 0, -1):
        print(f"\n... {i}")
        time.sleep(1)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("BOA SORTE A TODOS!\n")
    time.sleep(1)


def coletar_jogadores():
    """Coleta interativamente os nomes e funções dos jogadores."""
    jogadores = []
    print("\n--- Cadastro de Novos Jogadores ---")
    for funcao in funcoes + ["Coringa"]:
        while True:
            nome = input(f"Digite o nome de um jogador para a função '{funcao}' (ou Enter para pular): ")
            if not nome:
                break
            jogadores.append({"nome": nome, "funcao": funcao})
    # Validação para garantir que temos jogadores suficientes
    if len(jogadores) < 10:
        print(f"\nAVISO: Foram cadastrados apenas {len(jogadores)} jogadores. Pode não ser possível formar dois times completos.")
        time.sleep(2)
    return jogadores

def coringa(jogadores):
    """Separa a lista de jogadores em dois grupos: coringas e não coringas."""
    coringas = [j for j in jogadores if j["funcao"].lower() == "coringa"]
    nao_coringa = [j for j in jogadores if j["funcao"].lower() != "coringa"]
    return nao_coringa, coringas

def sortear_grupos(jogadores, funcoes):
    """Sorteia dois grupos balanceados, utilizando coringas e jogadores sobressalentes para preencher vagas."""
    nao_coringa, coringas = coringa(jogadores)
    por_funcao = {f: [] for f in funcoes}
    for jogador in nao_coringa:
        if jogador["funcao"] in por_funcao:
            por_funcao[jogador["funcao"]].append(jogador["nome"])

    grupo1, grupo2, jogadores_nao_alocados = [], [], []

    for funcao in funcoes:
        random.shuffle(por_funcao[funcao])
        if por_funcao[funcao]:
            grupo1.append({"nome": por_funcao[funcao].pop(0), "funcao": funcao})
        if por_funcao[funcao]:
            grupo2.append({"nome": por_funcao[funcao].pop(0), "funcao": funcao})
        jogadores_nao_alocados.extend([{"nome": nome, "funcao": funcao} for nome in por_funcao[funcao]])

    pool_de_reforco = coringas + jogadores_nao_alocados
    random.shuffle(pool_de_reforco)

    for time in [grupo1, grupo2]:
        while len(time) < 5 and pool_de_reforco:
            jogador_extra = pool_de_reforco.pop(0)
            funcoes_no_time = {j['funcao'] for j in time}
            funcao_faltando = next((f for f in funcoes if f not in funcoes_no_time), None)
            if funcao_faltando:
                time.append({"nome": jogador_extra['nome'], "funcao": funcao_faltando})
                
    return grupo1, grupo2

def exibir_grupos(grupo1, grupo2):
    """Imprime os dois grupos formatados no console."""
    print("--- TIMES SORTEADOS ---")
    print("\n🔵 GRUPO 1 🔵")
    for jogador in grupo1:
        print(f"  - {jogador['nome']} ({jogador['funcao']})")
    
    print("\n🔴 GRUPO 2 🔴")
    for jogador in grupo2:
        print(f"  - {jogador['nome']} ({jogador['funcao']})")
    print("-" * 25)
    print("feito por Thiago Pedriz.")


def main():
    """Função principal que executa o programa com um menu interativo."""
    jogadores_padrao = [
        {"nome": "Thiago", "funcao": "Mid laner"}, {"nome": "Paiva", "funcao": "Jungler"},
        {"nome": "João", "funcao": "Jungler"}, {"nome": "Tavares", "funcao": "Top laner"},
        {"nome": "Reche", "funcao": "Coringa"}, {"nome": "Miguel", "funcao": "Atirador"},
        {"nome": "Romeu", "funcao": "Top laner"}, {"nome": "Laércio", "funcao": "Atirador"},
        {"nome": "Yves", "funcao": "Atirador"}, {"nome": "Dente", "funcao": "Suporte"},
        {"nome": "Caio Rengar", "funcao": "Top laner"}, {"nome": "Vinícius", "funcao": "Suporte"},
        {"nome": "Castilho", "funcao": "Mid laner"}, {"nome": "Marcos", "funcao": "Coringa"}
    ]
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- SORTEIO DE TIMES 5x5 ---")
        print("Bem-vindo! O que deseja fazer?")
        print("\n1 - Sortear times com jogadores padrão")
        print("2 - Inserir novos jogadores e sortear")
        print("3 - Sair")
        
        escolha = input("\nDigite o número da opção desejada: ")
        
        jogadores_para_sorteio = None
        
        if escolha == "1":
            jogadores_para_sorteio = jogadores_padrao.copy()
            print("\nUsando jogadores padrão...")
            time.sleep(1)
            
        elif escolha == "2":
            jogadores_para_sorteio = coletar_jogadores()
            
        elif escolha == "3":
            print("Encerrando o programa. Bom jogo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(1.5)
            continue

        # Se uma opção válida de sorteio foi escolhida, executa o sorteio
        if jogadores_para_sorteio:
            grupo1, grupo2 = sortear_grupos(jogadores_para_sorteio, funcoes)
            animacao_loading()
            exibir_grupos(grupo1, grupo2)
            input("\nPressione Enter para voltar ao menu principal...")

if __name__ == "__main__":
    main()

