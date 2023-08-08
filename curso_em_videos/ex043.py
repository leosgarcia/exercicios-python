peso = float(input('Informe seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura ** 2)

if imc <= 18.5:
    resultado = 'ABAIXO DO PESO'
    print('Cuidado!')
elif imc <= 24.9:
    resultado = 'PESO IDEAL'
    print('Parabéns!')
elif imc <= 29.9:
    resultado = 'LEVEMENTE ACIMA DO PESO'
    print('Cuidado!')
elif imc <= 34.9:
    resultado = 'OBESIDADE GRAU I'
    print('Cuidado! Larga a cerveja.')
elif imc <= 39.9:
    resultado = 'OBESIDADE GRAU II (SEVERA)'
    print('Cuidado! Você está se arriscando.')
else:
    resultado = 'OBESIDADE GRAU III (MÓRBIDA)'
    print('Cuidado! você está quase morrendo.')

print('Seu IMC é {:.2f}. A classificação é: {}'.format(imc, resultado))
