nome = input ('Digite seu nome: ')
sobrenome = input ('Digite seu sobrenome: ')
idade = int (input ('Digite sua idade: '))
cont = 0
print(f'Nome:{nome} Sobrenome:{sobrenome} Idade:{idade}')

print('='*50)

if (idade < 18):
    print('Não pode usar o mercado Tech, para o que presta')
else:
    print ('Aproveite o mercado Tech')
    
print('='*50) 