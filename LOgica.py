def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas e colunas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador or \
           tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador or \
       tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False

def jogar_jogo_da_velha():
    tabuleiro = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    jogador_atual = 'X'

    while True:
        exibir_tabuleiro(tabuleiro)

        linha = int(input(f'Jogador {jogador_atual}, escolha a linha (0, 1, 2): '))
        coluna = int(input(f'Jogador {jogador_atual}, escolha a coluna (0, 1, 2): '))

        if tabuleiro[linha][coluna] == ' ':
            tabuleiro[linha][coluna] = jogador_atual

            if verificar_vitoria(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print(f'Parabéns! Jogador {jogador_atual} venceu!')
                break

            # Alternar para o próximo jogador
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'
        else:
            print('Essa posição já está ocupada. Escolha outra.')

# Executar o jogo
jogar_jogo_da_velha()