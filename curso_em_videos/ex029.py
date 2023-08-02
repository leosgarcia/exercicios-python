velocidade = int(input('Digite a velocidade: '))
limite = 80
taxa_multa = 7

if velocidade > limite:
    valor_multa = (velocidade - limite) * taxa_multa
    print('Você foi multado!')
    print(f'Valor da multa é R$ {valor_multa}')
    print('Tenha um bom dia. Dirija com segurança!')
else:
    print('Tenha um bom dia. Dirija com segurança!')