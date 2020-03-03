from operacoes_def import calc_soma, calc_sub, calc_mult, calc_div1, calc_div2, calc_resto, calc_raiz

num1 = int (input('Numero 1:'))
num2 = int (input('Numero 2:'))

print(f'Soma:{calc_soma (num1, num2)}')
print(f'Subtração:{calc_sub(num1, num2)}')
print(f'Multiplicação:{calc_mult(num1, num2)}')
print(f'Divisão inteira:{calc_div1(num1, num2)}')
print(f'Divisão Fracionada:{calc_div2(num1, num2)}')
print(f'Resto da divisão:{calc_resto(num1, num2)}')
print(f'Raiz:{calc_raiz(num1, num2)}')
