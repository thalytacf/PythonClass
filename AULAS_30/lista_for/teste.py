#EXERCICIOS DO DIA 13/11

#--- Exercício 1 - Listas
#--- Escreva programa que leia o nome de 10 alunos
#--- Armazene os nomes em uma lista
#--- Imprima a lista

#--- Exercício 2 - For
#--- Escreva programa que leia um número inteiro
#--- Calcule a taboada do número informado
#--- Imprima a taboada com a conta completa (n * i = r)

#--- Exercício 3 - Foreach
#--- Escreva programa que leia as notas (4) de 10 alunos
#--- Armazene as notas e os nomes em listas
#--- Imprima:
#           1- O nome dos alunos 
#           2- Média do aluno
#           3- Resuldo (Aprovado>=7.0)


lalunos = []

for i in range (0,10):
    lalunos.append (input(f'Nome do aluno {i+1}:'))
    n1 = int (input("Nota1: "))
    n2 = int (input("Nota2: "))
    n3 = int (input("Nota3: "))
    n4 = int (input("Nota4: "))