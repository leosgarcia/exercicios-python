from math import hypot, sqrt

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)
hipotenusa2 = sqrt((cateto_oposto * cateto_oposto) + (cateto_adjacente * cateto_adjacente))

print(f'A hipotenusa é: {hipotenusa:.2f}')
print(f'A hipotenusa é: {hipotenusa2:.2f}')


