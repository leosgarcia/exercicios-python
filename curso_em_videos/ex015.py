dias_locados = int(input('Quantos dias o carro ficou alugado? '))
km_rodados = int(input('Quantos kms foram rodados? '))

valor_dias = dias_locados * 60
valor_kms = km_rodados * 0.15

valor_total = valor_dias + valor_kms

print(f'O carro ficou {dias_locados} locados e rodou {km_rodados}km')
print(f'O valor a ser pago é R$ {valor_total:.2f}')