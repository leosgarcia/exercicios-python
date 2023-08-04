a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        triangulo = 'EQUILÁTERO'
    elif a != b and a != c and b != c:
        triangulo = 'EQUILÁTERO'
    else:
        triangulo = 'ISÓSCELES'
    print('Os segmentos informados podem formar um triângulo!')
    print(f'O triângulo formado é {triangulo}')
else:
    print('Os segmentos acima NÃO forma um triângulo')
