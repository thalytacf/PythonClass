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
