from random import choice
from time import sleep

# Lista de opções para jogar #
ARMAS = ('Pedra', 'Papel', 'Tesoura')

## Função para determinar o vencedor
def juiz_do_jogo(opcao_jogador, opcao_maquina):
    if opcao_jogador == opcao_maquina:
        return 'EMPATE'
    elif ((opcao_jogador == 'Pedra' and opcao_maquina == 'Tesoura') or 
          (opcao_jogador == 'Papel' and opcao_maquina == 'Pedra') or 
          (opcao_jogador == 'Tesoura' and opcao_maquina == 'Papel')):
         return 'VOCÊ VENCEU!'
    else:
        return 'MÁQUINA VENCEU!'


# Váraiaveis de pontuação #
pontuacao_jogador = 0
pontuacao_máquina = 0

# Variável de controle
n = 1

#Loop do jogo começa#
while n <= 3:
    if n == 1:
        pontuacao_jogador = 0
        pontuacao_máquina = 0

    # Jogador escolhe uma opção #
    print('Escolha sua arma para a jogada')
    print('-' * 30)
    for i in range(3):
        print(f'[{i+1}] - {ARMAS[i]}')
    print('-' * 30)

    opcao_jogador = int(input('Escolha o número da arma para jogar >>> '))
    opcao_jogador = ARMAS[opcao_jogador - 1]

    # Máquina escolhe uma opção #
    opcao_maquina = choice(ARMAS)

    # Programa mostra o resultado da partida #
    print('X' * 30)
    print(f'Você escolheu:      {opcao_jogador}')
    print(f'A Máquina escolheu: {opcao_maquina}')
    print('-' * 30)
    
    # Programa mostra quem ganhou a partida #
    resultado = juiz_do_jogo(opcao_jogador, opcao_maquina)
    print(resultado)
    print('=' * 30)
    print()
    sleep(3)
    # Pontuação do vencedor sobe
    if 'MÁQUINA' in resultado:
        pontuacao_máquina += 1
    if 'VOCÊ' in resultado:
        pontuacao_jogador += 1

    n += 1


# Quem vencer três vezes, ganha o jogo #
print('-' * 30)
print('Pontuação final')
print('-' * 30)
print(
f'''Jogador (Você) : {pontuacao_jogador} ponto(s)
Máquina : {pontuacao_máquina} ponto(s)''')
print()
if pontuacao_jogador > pontuacao_máquina:
    print('VOCÊ GANHOU O JOGO!')
elif pontuacao_máquina > pontuacao_jogador:
    print('MÁQUINA GANHOU O JOGO!')
else:
    print('O JOGO ACABOU EM EMPATE!')
