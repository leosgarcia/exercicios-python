import math
num = float(input('Digite um número: '))

parte_inteira_metodo1 = math.floor(num)
parte_inteira_metodo2 = num // 1
parte_inteira_metodo3 = math.trunc(num)
parte_inteira_metodo4 = int(num)

print(f'Numero inteiro: {parte_inteira_metodo1:.0f}')
print(f'Numero inteiro: {parte_inteira_metodo2:.0f}')
print(f'Numero inteiro: {parte_inteira_metodo3:.0f}')
print(f'Numero inteiro: {parte_inteira_metodo4}')
