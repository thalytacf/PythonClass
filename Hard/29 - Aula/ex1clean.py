def embarquecarro (motorista, passageiro):
    carro = []
    carro.append(motorista)
    carro.append(passageiro)
    return carro

def embarqueplat (pessoa, plataforma):
    plataforma.append(pessoa)
    return plataforma

def imprimir(sair, carro, entrar):
    print(f'Terminal: {terminal}')
    print(f'Ida: {fortwo}')
    print(f'Avião: {avião}')

def salvarterminal (plataforma):
    arquivoT = open('PythonHBSIS/Hard/29 - Aula/erminal.txt','a')
    arquivoT.append(f'{plataforma}\n')
    arquivoT.close()

def salvaraviao (plataforma):
    arquivoA = open('PythonHBSIS/Hard/29 - Aula/terminal.txt', 'a')
    arquivoA.append(f'{plataforma}\n')
    arquivoA.close()



print('#'*70)
print(f'Ida: Terminal - Avião \nVolta: Avião - Terminal')
print('#'*70)
pilotos = ['piloto','chefserv','policial']
pessoas = ['piloto','oficialA','oficialB','chefserv','comissariaA','comissariaB', 'policial','presidiario']

terminal = ''
avião = []
fortwo = []
terminal = pessoas
#salvarterminal(terminal)
############levar oficial A
fortwo = embarquecarro(pilotos[0],pessoas[1])
avião = embarqueplat(pessoas[1], avião)
del(terminal[1])
del(terminal[0])
imprimir(terminal,fortwo, avião)
#############levar oficial B
print('*'*70)
del(fortwo[1])
print(f'Volta: {fortwo}')
fortwo.clear()
fortwo = embarquecarro(pilotos[0],pessoas[0])
avião = embarqueplat(pessoas[0], avião)
del(terminal[0])
imprimir(terminal,fortwo, avião)
#############troca de motorista 
print('*'*70)
fortwo.clear()
fortwo = embarquecarro(pilotos[0],pessoas[0])
avião = embarqueplat(pilotos[0], avião)
del(terminal[0])
imprimir(terminal,fortwo, avião)
del(fortwo[0])
##############levar comi A
print('*'*70)
print(f'Volta: {fortwo}')
fortwo.clear()
fortwo = embarquecarro(pilotos[1],pessoas[0])
avião = embarqueplat(pessoas[0], avião)
del(terminal[0])
imprimir(terminal,fortwo, avião)
############# levar comi B
print('*'*70)
del(fortwo[1])
print(f'Volta: {fortwo}')
fortwo.clear()
fortwo = embarquecarro(pilotos[1],pessoas[0])
avião = embarqueplat(pessoas[0], avião)
del(terminal[0])
imprimir(terminal,fortwo, avião)
############# policia e preso
print('*'*70)
del(fortwo[1])
print(f'Volta: {fortwo}')
fortwo.clear()
fortwo = embarquecarro(pilotos[2],pessoas[1])
avião = embarqueplat(pessoas[1], avião)
avião = embarqueplat(pilotos[2], avião)
del(terminal[0])
del(terminal[0])
terminal.append(pilotos[1])
imprimir(terminal,fortwo, avião)
############troca de motorista 2 - buscar chefsev
print('*'*70)
fortwo.clear()
del(avião[2])
fortwo.append(pilotos[0])
print(f'Volta: {fortwo}')
fortwo = embarquecarro(pilotos[0],pilotos[1])
del(terminal[0])
avião = embarqueplat(pilotos[1], avião)
avião = embarqueplat(pilotos[0], avião)
imprimir(terminal,fortwo, avião)
#salvaraviao(avião)