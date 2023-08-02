santo = 'SANTO'
nascimento = input('Digite a cidade que você nasceu: ').upper()
nascimento.strip()
primeira_palavra = nascimento.split()

print(nascimento.strip())
print(primeira_palavra[0])
print(santo == primeira_palavra[0])