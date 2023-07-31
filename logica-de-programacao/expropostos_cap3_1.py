def calcula_media_ponderada(pesos, valores):
    soma_pesos = sum(pesos)
    soma_ponderada = sum(valores[i] * pesos[i] for i in range(len(valores)))
    media_ponderada = soma_ponderada / soma_pesos
    return media_ponderada


pesos = [1, 2, 3, 4, 5]
valores = []

for i in range(5):
    numero = float(input('Digite um número: '))
    valores.append(numero)

media = calcula_media_ponderada(pesos, valores)
print(f'A média ponderada dos número é: {media}')