distancia = float(input('Digite a distância de sua viagem: '))

if distancia > 200:
    preco = distancia * 0.45

else:
    preco = distancia * 0.50

print('Sua viagem de {}km vai custar R$ {}'.format(distancia, preco))