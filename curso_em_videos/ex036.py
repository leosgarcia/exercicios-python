valor_da_casa = float(input('Digite o valor da casa: '))
quantidade_de_anos = int(input('Em quantos anos você quer pagar a casa?'))
valor_do_salario = float(input('Digite o valor do seu salário: '))

prestacao = valor_da_casa / (quantidade_de_anos * 12)

if (valor_do_salario * 1.3) >= prestacao:
    print('Seu empréstimo foi aprovado.')
    print('O valor da parcela será de R$ {:.2f}'.format(prestacao))
else:
    print('Seu empréstimo fo negado!')

print('Tenha um bom dia!')
