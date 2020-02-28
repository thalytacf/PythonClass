lista = []
id = int(input('Digite seu id:'))
biografia = input('Digite sua biografia:')
interesses = input('Digite seus interesses:')
telefone = int(input('Digite seu telefone:'))
skype = input('Digite seu skype:')
dicionario = {'id':id, 'biografia':biografia, 'interesses':interesses, 'telefone':telefone, 'skype':skype}
lista.append(dicionario)

with open('C:/Users/900163/Desktop/git/PythonHBSIS/Hard/AulaX/table.txt', 'a') as arquivo:
    for p in lista:
        arquivo.write(f"{p['id']};{p['biografia']};{p['interesses']};{p['telefone']};{p['skype']}\n")