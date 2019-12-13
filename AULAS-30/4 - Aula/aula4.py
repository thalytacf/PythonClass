num1 = int(input('Digite um numero:'))
num2 = int(input('Digite outro numero:'))

print('='*50)

resultado1 = num1 + num2
resultado2 = num1 - num2
resultado3 = num1 * num2
resultado4 = num1 / num2

print (f'Soma: {resultado1}, Subtração: {resultado2}, Multiplicação: {resultado3 }, Divisão {resultado4}')

if(num1 > num2):
    maior = num1
    print('Maior: ', maior)
elif (num2>num1):
    maior = num2
    print('Maior: ', maior)
else:
    print('OS NUMEROS SÃO IGUAIS')

print('='*50)