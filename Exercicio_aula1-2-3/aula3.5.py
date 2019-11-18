#--- Exercicio 5  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia o salário de uma pessoa
#--- Use o método 50-20-10-20 - https://www.jaseimevirar.com/blog/como-voce-organiza-seu-orcamento-mensal/
#--- Informe os percentuais e valores que a pessoa deve utilizar em cada categoria

#Método 50-20-10-20 (50% gastos, 20% investimentos a longo prazo, 10% investimentos a curto prazo, 20% livre

salario = float(input('Salário:'))

gastos = (salario  * 0.5)
longop = (salario * 0.2)
curtop = (salario * 0.1)
livre = (salario * 0.2)

print (f' Gastos: {gastos} , Investimentos a longo prazo: {longop}, Investimentos a curto prazo {curtop} , Livre: {livre}')