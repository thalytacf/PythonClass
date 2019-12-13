#--- Exercício 2 - For
#--- Escreva programa que leia um número inteiro
#--- Calcule a taboada do número informado
#--- Imprima a taboada com a conta completa (n * i = r)

print ('='*70)

numero = int (input("Digite o numero para gerar a tabuada: "))
for i in range (0,11):
    print (f'{i} x {numero} = {i*numero}')

print ('='*70)