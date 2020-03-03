#--- Exercício 3 - Foreach
#--- Escreva programa que leia as notas (4) de 10 alunos
#--- Armazene as notas e os nomes em listas
#--- Imprima:
#           1- O nome dos alunos 
#           2- Média do aluno
#           3- Resuldo (Aprovado>=7.0)
print ('='*50)
lalunos = []
lnotas = []
n1 = 0
n2 = 1
n3 = 2
n4 = 3
for i in range (0,2):
    lalunos.append (input(f'Nome do aluno {i+1}:'))
    for j in range(0,4):
        lnotas.append (float(input(f'Nota{j+1}:')))

for aluno in lalunos:
    media = ((lnotas[n1] + lnotas[n2] + lnotas[n3] + lnotas[n4])/4)
    if (media >= 7):
        resultado = 'Aprovado'
    else:
        resultado = 'Reprovado'
    print ('='*50)
    print (f'Aluno: {aluno} Media:{media} Situação {resultado}')
    n1 += 4 
    n2 += 4
    n3 += 4
    n4 += 4
print ('='*50)