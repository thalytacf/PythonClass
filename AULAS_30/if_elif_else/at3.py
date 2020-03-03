print ("="*70)
print ("Bem vindo ao Mercado Tech")
produto = input("Nome do produto:")
categ = int(input ("Categoria do produto (1-Alcolico ou 2-Não alcoolico):"))

if(categ == 1):
    print ("Cadastro efetuado: {produto} Categoria: Alcoolico)
else:
    print ("Cadastro efetuado: {produto} Categoria: Não Alcoolico)
print ("="*70)