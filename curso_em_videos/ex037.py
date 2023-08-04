numero = int(input('Digite um número inteiro: '))
print('Escolha qual base de conversão deseja.')
base_de_coversao = int(input('[1] Binário - [2] Octal - [3] Hexa : '))

binario = bin(numero)
octal = oct(numero)
hexa = hex(numero)

if base_de_coversao == 1:
    print('O número {} em binário é: {}'.format(numero, binario[2:]))
elif base_de_coversao == 2:
    print('O número {} em binário é: {}'.format(numero, octal[2:]))
elif base_de_coversao == 3:
    print('O número {} em binário é: {}'.format(numero, hexa[2:]))
else:
    print('Digite um número válido!')
