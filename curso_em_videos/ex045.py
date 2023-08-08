from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura''')
jogador = int(input('Escolha uma opção: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)


print('-=' * 12)
print('O computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('-=' * 12)

if computador == 0:
    if jogador == 0:
        resultado = 'EMPATE'
    elif jogador == 1:
        resultado = 'JOGADOR GANHOU'
    elif jogador == 2:
        resultado = 'COMPUTADOR GANHOU'
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        resultado = 'COMPUTADOR GANHOU'
    elif jogador == 1:
        resultado = 'EMPATE'
    elif jogador == 2:
        resultado = 'JOGADOR GANHOU'
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        resultado = 'JOGADOR GANHOU'
    elif jogador == 1:
        resultado = 'COMPUTADOR GANHOU'
    elif jogador == 2:
        resultado = 'EMPATE'
    else:
        print('JOGADA INVÁLIDA!')

print('O resultado da da partida foi: {}'.format(resultado))