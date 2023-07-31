altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = largura * altura
litro_tinta = 2

tinta_necessaria = area / litro_tinta

print(f'Será necessário {tinta_necessaria} litros de tinta para pintar {area} m².')
