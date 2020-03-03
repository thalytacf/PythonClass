#--- 3 Crie um programa para calculo de investimento
#    Solicitar valor a ser investido no Tesouro selic
#    (Considerar valor do tesouro selic hoje 21/11) 5%
#    Calcular o valor total (valor investido + rendimento)
#    Considerar o vencimento do titulo(1/03/25)

from calc3 import calc_selic

qnt_cotas = float (input('Valor que deseja investir (>=0.01): '))

cota = 10410.00
valor_inv = qnt_cotas * cota

tesouro_selic = calc3(valor_inv)

print (f'Valor total do tesouro Selic: {tesouro_selic}')