nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media >=7:
    print('Sua média final foi {:.2f}. Você está APROVADO!'.format(media))
elif 5 <= media < 7:
    print('Sua média final foi {:.2f}. Você está de RECUPERAÇÃO!'.format(media))
else:
    print('Sua média final foi {:.2f}. Você está REPROVADO!'.format(media))
