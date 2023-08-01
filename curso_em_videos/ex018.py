import  math

angulo = float(input('Digite um ângulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O seno é: {seno:.2f}')
print(f'O cosseno é: {cosseno:.2f}')
print(f'A tangente é: {tangente:.2f}')