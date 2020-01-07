def embarquecarro (motorista, passageiro):
    carro = []
    carro.append(motorista)
    carro.append(passageiro)
    return carro

def embarqueplat (pessoa, plataforma):
    plataforma.append(pessoa)
    return plataforma

print('#'*70)
print(f'Ida: Terminal - Avião \nVolta: Avião - Terminal')
print('#'*70)
pilotos = ['piloto','chefserv','policial']
pessoas = ['piloto','oficialA','oficialB','chefserv','comissariaA','comissariaB', 'policial','presidiario']

terminal = ''
avião = []
fortwo = []
terminal = pessoas
############levar oficial A
fortwo = embarquecarro(pilotos[0],pessoas[1])
avião = embarqueplat(pessoas[1], avião)
del(terminal[1])
del(terminal[0])
print(f'Terminal: {terminal}')
print(f'Ida: {fortwo}')
print(f'Avião: {avião}')
#############levar oficial B
print('*'*70)
del(fortwo[1])
print(f'Volta: {fortwo}')
fortwo.clear()
fortwo = embarquecarro(pilotos[0],pessoas[0])
avião = embarqueplat(pessoas[0], avião)
del(terminal[0])
print(f'Terminal: {terminal}')
print(f'Ida: {fortwo}')
print(f'Avião: {avião}')
#############troca de motorista 
print('*'*70)
fortwo.clear()
fortwo = embarquecarro(pilotos[0],pessoas[0])
avião = embarqueplat(pilotos[0], avião)
del(terminal[0])
print(f'Terminal: {terminal}')
print(f'Ida: {fortwo}')
del(fortwo[0])
print(f'Avião: {avião}')
##############levar comi A
print('*'*70)
print(f'Volta: {fortwo}')
fortwo.clear()
fortwo = embarquecarro(pilotos[1],pessoas[0])
avião = embarqueplat(pessoas[0], avião)
del(terminal[0])
print(f'Terminal: {terminal}')
print(f'Ida: {fortwo}')
print(f'Avião: {avião}')
############# levar comi B
print('*'*70)
del(fortwo[1])
print(f'Volta: {fortwo}')
fortwo.clear()
fortwo = embarquecarro(pilotos[1],pessoas[0])
avião = embarqueplat(pessoas[0], avião)
del(terminal[0])
print(f'Terminal: {terminal}')
print(f'Ida: {fortwo}')
print(f'Avião: {avião}')
############# policia e preso
print('*'*70)
fortwo.clear()
fortwo = embarquecarro(pilotos[2],pessoas[1])
avião = embarqueplat(pessoas[1], avião)
avião = embarqueplat(pilotos[2], avião)
del(terminal[0])
del(terminal[0])
terminal.append(pilotos[1])
print(f'Terminal: {terminal}')
print(f'Ida: {fortwo}')
# avião.append(fortwo[1])
# avião.append(fortwo[0])
print(f'Avião: {avião}')
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
# avião.append(fortwo[1])
# avião.append(fortwo[0])
print(f'Terminal: {terminal}')
print(f'Ida: {fortwo}')
print(f'Avião: {avião}')