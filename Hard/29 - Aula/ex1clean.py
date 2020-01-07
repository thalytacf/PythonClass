###########PASSOS#########
#--- Add passageiros no fortwo
#--- Removo passageiros do fortwo do terminal
#--- Imprimo o carro cheio e o terminal
#--- Add o carona no avião
#--- Imprimo o carro avião
#--- TROCA DE MOTORISTA
#---
#---
motoristas = ['piloto','chefserv','policial']
passageiros = ['oficialA','oficialB','comissariaA','comissariaB','presidiario']
aviao = []
fortwo = []
terminal = []

################# MAIN ##############

terminal.append(passageiros)
terminal.append(motoristas)
del(terminal[0][0])

print(showterminal(terminal))
print(f' Terminal - Avião: {addcarro(motoristas[0], passageiros[0])}')
print(showaviao(aviao))



################# METODO ENCHER CARRO
def addcarro (pass1, pass2):
    carro = []
    carro.append(pass1)
    carro.append(pass2)
    return carro

################# METODO SHOW PLACES

def showaviao (aviao):
    print(f'Avião: {aviao}')

def showterminal (terminal):
    print(f'Terminal: {terminal}')

################# METODO LIMPAR

def clearthis (elemento):
    elemento.clear()
    return elemento

def sairterminal (terminal):
    del(terminal[0][0])
    return terminal


pilotos = ['piloto','chefserv','policial']
pessoas = ['piloto','oficialA','oficialB','chefserv','comissariaA','comissariaB', 'policial','presidiario']

terminal = ''
avião = []
fortwo = []
terminal = pessoas
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
print('*'*70)
fortwo.clear()
del(avião[2])
fortwo.append(pilotos[0])
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
