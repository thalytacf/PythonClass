class Endereco:
    id = 0
    rua = ''
    numero = ''
    complemento = ''
    baiiro = ''
    cidade = ''

    def exportar_txt(self, lista_enderecos):
        #----- Cria um arquivo e atribui a uma variável 'arquivo'
        with open('/Users/900163/Desktop/PythonHBSIS/Hard/ENDERECO/enderecosY.txt','a') as arquivo:
            #---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
            for x in lista_enderecos:
                arquivo.write(f"{str(x)}\n")

    def __str__(self):
        #Para transforar em string
        return f'{self.id};{self.rua};{self.numero};{self.complemento};{self.baiiro};{self.cidade}'