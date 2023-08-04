from datetime import date

ano_de_nascimento = int(input('Digite o ano de seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_de_nascimento
idade_de_alistamento = 18

print('Quem nasceu em {} tem {} anos em {}'.format(ano_de_nascimento, idade, ano_atual))
print('Você é do sexo Masculino ou Feminino?')
print('[ 1 ] - Macuslino')
print('[ 2 ] - Feminino')
sexo = int(input('Escolha a opção: '))

if sexo == 1:
    if idade < idade_de_alistamento:
        anos_faltantes = idade_de_alistamento - idade
        print('Ainda faltam {} anos para você se alistar.'.format(anos_faltantes))
        print('Você se alistará apenas em {}'.format(ano_atual + anos_faltantes))
    elif idade == idade_de_alistamento:
        print('Você deve se alistar IMEDIATAMENTE pois completou {} anos!'.format(idade_de_alistamento))
    else:
        print('Você está com o alistamento militar ATRASADO! Regularize-se.')
elif sexo == 2:
    print('Pessoas do sexo feminino não são obrigadas a se alistar.')
else:
    print('Escolha uma opção válida!')