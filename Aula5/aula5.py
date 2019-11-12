n1 = int (input("Agrege um valor a N1:"))
n2 = int (input("Agrege um valor a N2:"))
n3 = int (input("Agrege um valor a N3:"))
n4 = int (input("Agrege um valor a N4:"))

if (n1>n2 and n1>n3 and n1>n4):
    maior = n1
elif (n2>n1 and n2>n3 and n2>n4):
    maior = n2
elif (n3>n2 and n3>n1 and n1>n4):
    maior = n3
else:
    maior = n4
print ("Maior nota: ", maior)

if (n1<n2 and n1<n3 and n1<n4):
    menor = n1
elif (n1>n2 and n1>n3 and n1>n4):
    menor = n1
elif (n2>n1 and n2>n3 and n2>n4):
    menor = n2
elif (n1>n2 and n1>n3 and n1>n4):
    menor = n3
else:
    menor = n4
print ("Menor nota: ", menor)):




