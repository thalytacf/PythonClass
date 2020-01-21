class Squad:
    self.id = 0
    self.nome = ''
    self.descricao = ''
    self.numpessoas = 0
    self.backend = ''
    self.frontend = ''

    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.numpessoas};{self.backend};{self.frontend}'