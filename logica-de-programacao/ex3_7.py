
for i in range(1, 10):
    numero = int(input('Digite um número: '))
    if (i == 1):
        maior = numero
        menor = numero
    else:
        if(numero > maior):
            maior = numero
        elif(numero < menor):
            menor = numero

print(f'O número {menor} é o menor número digitado!')
print(f'O número {maior} é o maior número digitado!')

