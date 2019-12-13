#___Validação com Booleano
print('='*70)
ativo = True

if (ativo):
    print('Logar')
else:
    print('Não pode')

print('='*70)
#___Criação de variavel booleana através de expressões (validação)
idade = 18

validador = (idade == 18)
print (validador)
validador = (idade != 18)
print (validador)
validador = (idade > 18)
print (validador)
validador = (idade < 18)
print (validador)
validador = (idade >= 18)
print (validador)
validador = (idade <= 18)
print (validador)

print('='*70)

#___Validação com variaveis not, and e or
validador = not True
validador = not False

validador = (idade > 18 and idade < 18)
validador = (idade > 18 or idade == 18)

print('='*70)