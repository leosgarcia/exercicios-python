from random import choice

aluno1 = input('Digite o primeiro aluno: ')
aluno2 = input('Digite o segundo aluno: ')
aluno3 = input('Digite o terceiro aluno: ')
aluno4 = input('Digite o quarto aluno: ')

lista_alunos = [aluno1, aluno2, aluno3, aluno4]

escolhido = choice(lista_alunos)

print(f'O aluno escolhido foi: {escolhido}')
