def criar_faixa (mus, art, alb):
    dic_faixa = {'musica': mus, 'artista':art, 'album':alb}
    return dic_faixa

def salvar_faixa(faixa):
    arquivo = open('PythonHBSIS/Aula16/faixas.txt', 'a')
    arquivo.write(f"{faixa['musica']};{faixa['artista']};{faixa['album']} \n")
    arquivo.close()

def ler_faixa ():
    arquivo = open('PythonHBSIS/Aula16/faixas.txt', 'r')
    lista_faixas = []
    for linha in arquivo:
        linha = linha.strip()
        dados_faixa = linha.split(';')
        faixa = criar_faixa(dados_faixa[0], dados_faixa[1], dados_faixa[2])
        lista_faixas.append(faixa)
    arquivo.close()
    return lista_faixas

