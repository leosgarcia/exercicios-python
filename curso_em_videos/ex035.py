a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a + b > c and a + c > b and b + c > a:
    print('\033[0;33;44mOs acima segmentos podem formar um triângulo!\033[m')
else:
    print('Os segmentos acima NÃO forma um triângulo')
