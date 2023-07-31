n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisao_inteira = n1 // n2
divisao_resto = n1 % n2
potencia = n1**n2 

print(f'A soma de {n1} e {n2} é {soma}')
print(f'A subtração de {n1} e {n2} é {subtracao}')
print(f'A multiplicação de {n1} e {n2} é {multiplicacao}')
print(f'A divisão de {n1} e {n2} é {divisao}')
print(f'{n1} divido por {n2} é {divisao_inteira}')
print(f'O resto da divisão é {n1} e {n2} é {divisao_resto}')
print(f'{n1} elevado à {n2} é {potencia}')
