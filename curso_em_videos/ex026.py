frase = input('Digite uma frase: ').upper().strip()

print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira aparição da letra A é na posição {} no texto'.format(frase.find('A') + 1))
print('A última aparição da letra A é na posição {} no texto'.format(frase.rfind('A') + 1))
