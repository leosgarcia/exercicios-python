from datetime import date

ano_de_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_de_nascimento

if idade <= 7:
    classificacao = 'MIRIM'
elif idade <= 14:
    classificacao = 'INFANTIL'
elif idade <= 19:
    classificacao = 'JÚNIOR'
elif idade <= 25:
    classificacao = 'SÊNIOR'
else:
    classificacao = 'MASTER'

print(f'Classificação: {classificacao}')
