def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input('Digite um número: '))

if eh_primo(num):
    print(f'O número {num} é primo!')
else:
    print(f'O número {num} não é primo!')
