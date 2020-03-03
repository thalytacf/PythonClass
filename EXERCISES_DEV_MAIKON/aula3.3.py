#--- Exercicio 3  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia os dados de um funcionário
#--- Funcionário: Nome Completo, CPF, Número do registro, Cargo e Salário
#--- Exiba os dados de salário liquido, descontando os tributos
#--- Deve ser calculado o valor do INSS -
#--- INSS -  de    0,00 ate 1751,81 - percetual =  8,0%
#---         de 1751,82 ate 2919,72 - percetual =  9,5%
#---         de 2919,72 ate 5839,45 - percetual = 11,0%
#--- Deve ser calculado o valor do IRRf - 
#--- IRRF -  de    0,00 ate 1903,98 - percetual =  0,0%
#---         de 1903,98 ate 2826,65 - percetual =  7,5%
#---         de 2826,66 ate 3751,05 - percetual = 15,0%
#---         de 3751,06 ate 4664,68 - percetual = 22,5%
#---         de 4664,69 ate ------- - percetual = 27,5%
#--- Base - http://www.calculador.com.br/calculo/salario-liquido 
# nome_completo = input('Digite seu nome completo: ')
# cpf = input('Digite seu CPF: ')
# num_registro = input('Digite seu registro: ')
# cargo = input('Digite seu cargo: ')
# salario = float(input('Digite seu salario: '))


from calc_imposto import
print ('='*50)

salario = float(input('Digite seu salario: '))
#essas variaveis independe do metodo
#salvando o retorno em uma variavel
inss= calculo_inss(salario)
irrf = calc_irrf(salario, inss)
salario_lqd = salario - inss - irrf 




print ('='*50)
print(f'INSS:{inss}')
print(f'IRRF:{irrf}')
print (f'Seu salario liquido é {salario_lqd}')
print ('='*50)