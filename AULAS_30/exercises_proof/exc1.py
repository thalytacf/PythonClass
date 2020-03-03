#--- 1 Crie um programa que calcule o 
#--- imposto de ISS de um serviço de desenvolvimento de software
#--- Utilizar metodos

from calc1 import *

valor_iss= float(input('Valor do Seviço: '))

iss = calc_iss(valor_iss)
print(f'Valor do iss: {iss}')
