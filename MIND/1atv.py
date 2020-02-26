'''
Um espaço binário dentro de um número inteiro positivo N é qualquer sequência máxima de zeros consecutivos
que está rodeado por 1 dos dois lados na representação binária de N.

Por exemplo, o número 9 tem representação binária 1001 e contém uma lacuna binária de comprimento 2.
O número 529 tem representação binária 1000010001 e contém duas lacunas binárias:
um de comprimento 4 e um de comprimento 3.
O número 20 tem representação binária 10100 e contém um espaço binário de comprimento 1.
O número 15 tem representação binária 1111 e não possui lacunas binárias.
O número 32 tem representação binária 100000 e não possui lacunas binárias.

Escreva uma função:

solução def (N)

que, dado um número inteiro positivo N, retorna o comprimento de seu maior intervalo binário.
A função deve retornar 0 se N não contiver um espaço binário.

Exemplo, dado N = 1041, a função deve retornar 5,
porque N tem representação binária 10000010001 e, portanto, seu maior intervalo binário tem o comprimento 5.

Dado N = 32, a função deve retornar 0, porque N tem representação binária '100000'
e, portanto, sem lacunas binárias.
'''

# class Binario:
#     def __init__(self, n):
#         self.n = n
#
#     def contar(self):
#         num = bin(self.n)
#         lista_num = []




def insere_bin_lista(numero):
    numero_bin = bin(numero)
    convert_bin_to_str = numero_bin.__str__()
    lista_bin = [int(bin) for bin in convert_bin_to_str]
    lista_bin.pop(0)[2:]
    lista_bin.pop(0)
    return lista_bin


lista_binarios = insere_bin_lista(20)
print(lista_binarios)

def logica_binario(lista_binarios):
    if lista_binarios.__contains__('0'):
        print('tem zero')
    else:
        print('Só tem o número 1')
        # if lista_binarios.index('1') == '0':
        #     lista_binarios.pop(0)

print()
