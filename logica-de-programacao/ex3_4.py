num = int(input('Digite um número: '))
acumulador = 0

for i in range(1,num + 1):
    acumulador += (1 / i)

print(acumulador)