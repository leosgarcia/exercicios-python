nome = input('Digite seu nome: ').strip()

print('Analisando seu nome!')
print(f'Seu nome em maiúscula é: {nome.upper()}')
print(f'Seu nome em minúscula é: {nome.lower()}')
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

nome_separado = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(nome_separado[0], len(nome_separado[0])))
