from random import randint
from time import sleep

numero = randint(0, 5)
print('-=-' * 13)
print('Tente adivinhar o número que eu pensei.')
print('-=-' * 13)

chute = int(input('Digite um número entre 0 e 5: '))

print('Processando...')
sleep(3)

if numero == chute:
    print('Você acertou!')
    print(f'O seu chute de número {chute} é igual ao número {numero} que pensei.')
else:
    print('Você errou!')
    print(f'O seu chute de número {chute} é igual ao número {numero} que pensei.')
