# Sorteador de Times para Jogos 5v5

![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)

Um script de linha de comando em Python para sortear dois times balanceados para jogos 5v5 (como League of Legends, Valorant, etc.). A ferramenta possui uma lógica inteligente para alocar jogadores com base em suas funções principais e utilizar "Coringas" para preencher as vagas restantes.

---

## ✨ Funcionalidades

* **Alocação por Role Principal:** Garante que os times sejam formados, primeiramente, com jogadores em suas posições de ofício.
* **Sistema de "Coringa" (Fill):** Jogadores marcados como "Coringa" são alocados de forma inteligente nas posições que faltam em cada time.
* **Tratamento de Excedentes:** Lida com cenários onde há um número ímpar de jogadores para uma mesma função, reaproveitando os jogadores sobressalentes.
* **Menu Interativo:** Permite ao usuário sortear novamente, inserir uma nova lista de jogadores ou encerrar o programa de forma amigável.
* **Dois Modos de Operação:**
    1.  **Padrão:** Inicia com uma lista de jogadores pré-definida no código para testes rápidos.
    2.  **Manual:** Permite cadastrar todos os jogadores e suas funções interativamente.

---

## 🚀 Como Usar

### Pré-requisitos

* Python 3.7 ou superior instalado.

### Instalação

1.  Clone este repositório para a sua máquina local:
    ```bash
    git clone [https://github.com/TPedriz/Sorteio-times-x5.git](https://github.com/TPedriz/Sorteio-times-x5.git)
    ```
2.  Navegue até o diretório do projeto:
    ```bash
    cd Sorteio-times-x5
    ```

### Executando o Script

Para iniciar o programa, basta executar o arquivo Python no seu terminal:

```bash
python nome_do_arquivo.py
```

O script irá sortear os times com a lista padrão e, em seguida, exibirá o menu de opções.

---

## 🎮 Exemplo de Uso

Ao executar o script, a saída no terminal será semelhante a esta:

```text
--- TIMES SORTEADOS ---

🔵 GRUPO 1 🔵
  - Player 1 (Top laner)
  - Player 2 (Jungler)
  - Player 3 (Mid laner)
  - Player 4 (Atirador)
  - Player 5 (Suporte)

🔴 GRUPO 2 🔴
  - Player 6 (Top laner)
  - Player 7 (Jungler)
  - Player 8 (Mid laner)
  - Player 9 (Atirador)
  - Player 10 (Suporte)
-------------------------

O que deseja fazer?
1 - Sortear de novo com os mesmos jogadores
2 - Inserir novamente o nome dos jogadores
3 - Sair
Digite o número da opção desejada:
```

---

## 🏗️ Estrutura do Código

O código é modularizado em funções para garantir clareza e manutenibilidade:

* `main()`: Orquestra a execução principal do programa e gerencia o menu interativo.
* `sortear_grupos()`: Contém a lógica central para separar e balancear os times, incluindo o tratamento de coringas e excedentes.
* `coletar_jogadores()`: Responsável por gerenciar a entrada de dados do usuário no modo manual.
* `coringa()`: Uma função utilitária para separar jogadores "Coringa" dos demais.
* `exibir_grupos()`: Formata e imprime a composição final dos times no console.

---

## 👤 Autor

* **Thiago Pedriz** - [GitHub/TPedriz](https://github.com/TPedriz)
