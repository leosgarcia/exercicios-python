num = int(input('Digite um número: '))
fatorial = 1

for i in range(num):
    fatorial = fatorial * (i + 1)

print(f'O fatorial de {num} é {fatorial}')