# Aula 19 - 04-12-2019
# Lista com for e metodos

# 1 - Com a seguinte lista imprima na tela (unsado a indexação e f-string) 

cadastroHBSIS = ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                ]


# nome  Alex telefone: 4799991
# idade Carlos é 15 anos
# email de Mateus é d@d.com
cab = cadastroHBSIS[0::2]
dados = cadastroHBSIS[1::2]
print('='*30)
print(f'{cab[0]}:{dados[0][0]} {cab[1]}: {dados[1][0]}')
print(f'{cab[3]} de {dados[0][4]} é {dados[3][4]} anos')
print(f'{cab[2]} de {dados[0][3]} é {dados[2][3]}')
print('='*30)
# 2 - usando o for, imprima todos nomes um abaixo do outro
i=-1
for i in range(7):
    print(f'{dados[0][i]}')
    i = i+1
print('='*30)
 

# 3 - Usando a indexação faça uma lista com 3 dicionarios contendo os dados do Mateus, Paulo e João
#  contendo como chaves: nome, email, idade, telefone (nesta  sequencia)

# dic1 = {'nome':dados[0][3], 'email':dados[2][3], 'idade':dados[3][3], 'telefone':dados[1][3]}
# dic2 = {'nome':dados[0][1], 'email':dados[2][1], 'idade':dados[3][1], 'telefone':dados[1][1]}
# dic3 = {'nome':dados[0][5], 'email':dados[2][5], 'idade':dados[3][5], 'telefone':dados[1][5]}

lista = []
# lista.append(dic1)
# lista.append(dic2)
# lista.append(dic3)

# print(lista)
# print('='*30)

##################
for indice_lento in range(7):
    dic = {}
    for indice_rapido in range(4):
        dic[cab[indice_rapido]] = dados[indice_rapido][indice_lento]
    lista.append(dic)
                                                                            
for i in lista:
    print(i)