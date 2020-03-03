# Ex aleatórios

a = bin(25)

lista = list()
lista = [x for x in a[2:]]
print(lista)

for vezes in range(2):
    n = lista.pop(-1)
    lista.insert(0, n)

a = ''
for item in lista:
    a.join(item)
print(a)

#alteração para commit
