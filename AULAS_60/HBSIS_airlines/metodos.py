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

def delprint(carro):
    del(carro[1])
    print(f'Volta: {carro}')

def salvarterminal (plataforma):
    arquivoT = open('PythonHBSIS/Hard/29 - Aula/terminal.txt','w')
    arquivoT.write(f'{plataforma}\n')
    arquivoT.close()

def salvaraviao (plataforma):
    arquivoA = open('PythonHBSIS/Hard/29 - Aula/aviao.txt', 'w')
    arquivoA.write(f'{plataforma}\n')
    arquivoA.close()