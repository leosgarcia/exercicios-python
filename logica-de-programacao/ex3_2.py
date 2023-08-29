
num = int(input('Digite um número: '))
raiz_aproximada = 0

while ((raiz_aproximada * raiz_aproximada) < num):
    raiz_aproximada += 1

raiz_aproximada -= 1

print(f'Inteiro aproximado da raíz quadrada de {num} é {raiz_aproximada}')
