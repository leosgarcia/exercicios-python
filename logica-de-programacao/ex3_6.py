num = int(input('Digite um número: '))

a = 1
b = 1
c = 0

print(a)
print(b)
for i in range(num - 2):
    c = a + b
    print(c)
    a = b
    b = c
