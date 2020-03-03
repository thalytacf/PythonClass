######### METODOS

from faixa import criar_faixa, salvar_faixa, ler_faixa


#cadastro de playlist
#lendo musica, artista e album

musica = input('Digite uma musica: ')
artista = input('Digite uma artista: ')
album = input('Digite uma album: ')

dicionario_faixa = criar_faixa(musica, artista, album)

salvar_faixa(dicionario_faixa)

lista = ler_faixa()

for faixa in lista:
    print(f"{faixa['musica']} - {faixa['artista']} -  {faixa['album']} ")