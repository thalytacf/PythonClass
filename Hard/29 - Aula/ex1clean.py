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


<<<<<<< HEAD

print('#'*70)
print(f'Ida: Terminal - Avião \nVolta: Avião - Terminal')
print('#'*70)
=======
def sairterminal (terminal):
    del(terminal[0][0])
    return terminal


>>>>>>> 8d0f3ed97996511e7cb5cb281d70560204a075f3
pilotos = ['piloto','chefserv','policial']
pessoas = ['piloto','oficialA','oficialB','chefserv','comissariaA','comissariaB', 'policial','presidiario']

terminal = ''
avião = []
fortwo = []
terminal = pessoas
<<<<<<< HEAD
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
=======
############

print(f'Avião - Terminal: {fortwo}')
fortwo.append(pilotos[0])
fortwo.append(pessoas[1])
del(terminal[1])
del(terminal[0])
avião.append(fortwo[1])
print(f'Terminal: {terminal}')
print(f'Terminal - Avião {fortwo}')
print(f'Avião: {avião}')
#############
print('*'*70)
del(fortwo[1])
print(f'Avião - Terminal: {fortwo}')
fortwo.append(pessoas[0])
del(terminal[0])
avião.append(fortwo[1])
print(f'Terminal: {terminal}')
print(f'Terminal - Avião {fortwo}')
print(f'Avião: {avião}')
#############troca de motorista
print('*'*70)
fortwo.clear()
fortwo.append(pilotos[0])
fortwo.append(pessoas[0])
del(terminal[0])
avião.append(fortwo[1])
print(f'Terminal: {terminal}')
print(f'Terminal - Avião {fortwo}')
print(f'Avião: {avião}')
##############
print('*'*70)
fortwo.clear()
print(f'Avião - Terminal: {fortwo}')
fortwo.append(pilotos[1])
fortwo.append(pessoas[0])
del(terminal[0])
avião.append(fortwo[1])
print(f'Terminal: {terminal}')
print(f'Terminal - Avião {fortwo}')
print(f'Avião: {avião}')
#############
print('*'*70)
del(fortwo[1])
print(pessoas)
print(f'Avião - Terminal: {fortwo}')
fortwo.append(pessoas[0])
del(terminal[0])
avião.append(fortwo[1])
print(f'Terminal: {terminal}')
print(f'Terminal - Avião {fortwo}')
print(f'Avião: {avião}')
#############
print('*'*70)
fortwo.clear()
fortwo.append(pilotos[2])
fortwo.append(pessoas[1])
del(terminal[0])
del(terminal[0])
terminal.append(pilotos[1])
print(f'Terminal: {terminal}')
print(f'Terminal - Avião {fortwo}')
avião.append(fortwo[1])
avião.append(fortwo[0])
print(f'Avião: {avião}')
############troca de motorista 2
>>>>>>> 8d0f3ed97996511e7cb5cb281d70560204a075f3
print('*'*70)
fortwo.clear()
del(avião[2])
fortwo.append(pilotos[0])
<<<<<<< HEAD
print(f'Volta: {fortwo}')
fortwo = embarquecarro(pilotos[0],pilotos[1])
del(terminal[0])
avião = embarqueplat(pilotos[1], avião)
avião = embarqueplat(pilotos[0], avião)
imprimir(terminal,fortwo, avião)
#salvaraviao(avião)
=======
print(f'Avião - Terminal: {fortwo}')
fortwo.append(terminal[0])
del(terminal[0])
avião.append(fortwo[1])
avião.append(fortwo[0])
print(f'Terminal: {terminal}')
print(f'Avião: {avião}')

def embarquecarro (motorista, passageiro):
    carro = []
    carro.append(motorista)
    carro.append(passageiro))
    return carro

def embarqueplat (pessoa, plataforma):
    plataforma.append(pessoa)
    return plataforma


################# METODO CARRO LIMPO

# def clearcar (carro):
#     carro.clear()
#     print(f'Aviao - Terminal: {carro}')

################# METODO ENCHER CARRO

#def addcar (pass1, pass2, carro):
#    carro.append(pass1)
#    carro.append(pass2)
#    print(f' Terminal - Avião: {carro}')

################# METODO SHOW PLACES
#def showaviao (aviao):
#    print(f'Avião: {aviao}')

#def showaviao (terminal):
#    print(f'Terminal: {terminal}')
>>>>>>> 8d0f3ed97996511e7cb5cb281d70560204a075f3
