from math import sqrt

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

delta = ((b ** 2) - (4 * a * c))
x1 = (-b + sqrt(delta)) / (2 * a)
x2 = (-b - sqrt(delta)) / (2 * a)

print('O valor de delta é: {}'.format(delta))
print('O valor de x1 é: {}'.format(x1))
print('O valor de x2 é: {}'.format(x2))
