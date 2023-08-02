nome = input('Digite seu nome completo: ').strip()
nome = nome.upper()
nome_separado = nome.split()

print('Analisando o nome: {}'.format(nome))
print('SILVA' in nome_separado)

print('SILVA' in nome.upper())

