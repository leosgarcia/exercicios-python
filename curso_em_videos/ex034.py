salario = float(input('Digite o valor do seu salário: '))

if salario > 1250:
    aumento = salario * 1.10
else:
    aumento = salario * 1.15

print('Salário antigo R$ {}. Seu novo salário é de R$ {:.2f}'. format(salario, aumento))