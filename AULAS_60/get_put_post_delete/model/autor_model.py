import sqlalchemy as db
from sqlalchemy.orm import relationship

from Hard.Aula55.model import Pessoa
#from Aula55.model.base import Base
#from Aula55.dao.pessoa_dao import PessoaDao

class Autor(Base):
    __tablename__ = "livraria_autor"
    id = db.Column(db.Integer, primary_key=True)
    pseudonimo = db.Column(db.String(45))
    descricao = db.Column(db.String(100))
    pessoa_id = db.Column(db.Integer, db.ForeignKey('livraria_pessoa.id'))
    pessoa = relationship(Pessoa)
