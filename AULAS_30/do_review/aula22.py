# print('em range')
# for i in range (1, 100, 2)
#     print(i)

# print('em lista')
# i in [1,2,3,4,5,6]:
#     print(i)

# print('em texto')
# for i in 'TEXTO'
#     print(i)

#############################################
dia_cada_mês = {
1:31
2:28
3:31
4:30
5:31
6:30
7:31
8:31
9:30
10:31
11:30
12:31
}

qual_mes = int(input('Digite o mês (1-12):'))

total = 0
for  tempo range (qual_mes, 12+1):
    total+= dia_cada_mês[mes]
    
print('Total até o fim do ano =', total)


