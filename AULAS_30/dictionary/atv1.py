#Ler os dados da cerveja
#Cerveja: Marca, Tipo, IBU, ABV, EBC, VOLUME
#Crie um dicionario para armazenar os dados
#Impreima os dados do dicionario

marca = (input('Marca:'))
tipo = (input('Tipo:'))
ibu = (input('IBU:'))
abv = (input('ABV:'))
ebc = (input('EBC:'))
volume = int(input('Volume:'))
dicionario = {'marca':marca, 'tipo':tipo ,'ibu': ibu , 'abv':abv , 'ebc':ebc ,'volume':volume}
print (f"{dicionario['marca']}-{dicionario['tipo']}-{dicionario['ibu']}-{dicionario['abv']}-{dicionario['volume']}")