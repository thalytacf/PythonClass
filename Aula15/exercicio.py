#arquivo = open('aula15test.txt','x')
def salvar_pessoa(cerv_dicionario):
  arquivo = open('aula15test.txt','a')
  arquivo.write(f"{cerv_dicionario['nome']};{cerv_dicionario['marca']};{cerv_dicionario['tipo']};{cerv_dicionario['teor']}\n")
  arquivo.close()

def ler():
  lista = []
  arquivo = open('aula15test.txt','r')
  for linha in arquivo:
    linha = linha.strip()
    lista_linha = linha.split(';')
    cerveja = {'nome':lista_linha[0], 'marca':lista_linha[1], 'tipo':lista_linha[2], 'teor':lista_linha[3]}
    lista.append(cerveja)
  arquivo.close()
  return lista

for cerveja in ler():
  print(f"{cerveja['nome']} - {cerveja['marca']} - {cerveja['tipo']} - {cerveja['teor']}")
