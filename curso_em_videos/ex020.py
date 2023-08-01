from random import shuffle

aluno1 = input('Digite o primeiro aluno: ')
aluno2 = input('Digite o segundo aluno: ')
aluno3 = input('Digite o terceiro aluno: ')
aluno4 = input('Digite o quarto aluno: ')

lista_alunos = [aluno1, aluno2, aluno3, aluno4]

shuffle(lista_alunos)

print(f'A ordem será: ')
print(lista_alunos)
