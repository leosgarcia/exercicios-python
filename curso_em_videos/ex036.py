valor_da_casa = float(input('Digite o valor da casa: '))
quantidade_de_anos = int(input('Digite em quantos anos você quer pagar a casa: '))
valor_do_salario = float(input('Digite o valor do seu salário: '))

prestacao = valor_da_casa / (quantidade_de_anos * 12)
limite_do_emprestimo = valor_do_salario * 0.3

print(limite_do_emprestimo)

if limite_do_emprestimo >= prestacao:
    print('Seu empréstimo foi aprovado.')
    print('O valor da parcela será de R$ {:.2f}'.format(prestacao))
else:
    print('Seu empréstimo fo negado!')

print('Tenha um bom dia!')
