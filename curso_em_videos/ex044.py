compras = float(input('Digite o valor da compra: '))
print('========= LOJÃO DO TONHÃO =========')
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/débito')
print('[ 2 ] à vista cartão de crédito')
print('[ 3 ] 2x no cartão de crédito')
print('[ 4 ] 3x ou mais no cartão de crédito')
opcao = int(input('Escolha uma opção: '))

if opcao == 1:
    total = compras - (compras * (10 / 100))
elif opcao == 2:
    total = compras - (compras * (5 / 100))
elif opcao == 3 or opcao == 4:
    parcelas = int(input('Em quantas parcelas será o pagamento? Insira aqui: '))
    if parcelas > 2:
        juros = compras * (20 / 100)
        total = compras + juros
        print('Sua compra parcelada em {}x de R$ {}'.format(parcelas, juros))
    else:
        total = compras
else:
    print('Opção inválida!')

print('O valor a ser pago será de R${}'.format(total))
