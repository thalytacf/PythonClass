#---2 Crir um programa que calcule
# a rentabilidade anual de um investimento 
# baseando -se em sua rentablidade mensal (justos composto)
# a rentabilidade deve ser apresentada em % em R$
#--- Utilizar metodos

from calc2 import calc_montante

capital = float(input('Valor investdo: '))
taxa_mensal = float(input('Taxa mensal: '))
prazo = int(input('Prazo (em anos): '))

r_montante = calc_montante(montante)
r_taxa_anual = calc_montante(taxa_anual)

print(f'Montante: R${r_montante}')
print(f'Rendimento: {r_taxa_anual}%')