nome = input('Digite seu nome completo: ').strip().upper()
nome_quebrado = nome.split()

print(nome_quebrado)

print('Seu primeiro nome é: {}'.format(nome_quebrado[0]))
print('Seu último nome é: {}'.format(nome_quebrado[-1]))
print('Seu último nome é: {}'.format(nome_quebrado[len(nome_quebrado) - 1]))
