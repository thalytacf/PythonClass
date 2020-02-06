import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PessoaModel(Base):
    __tablename__ = 'pessoas'

    id = db.Column(db.Integer(11), primary_key=True)
    nome = db.Column(db.String(45))
    sobrenome = db.Column(db.String(45))
    idade = db.Column(db.Integer(11))

    def __str__(self):
        return f"{self.id} -- {self.nome} -- {self.sobrenome} -- {self.idade}"
