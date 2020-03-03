import sqlalchemy as db

#from Aula55.model.base import Base

class Pessoa(Base):
    __tablename__ = 'LIVRARIA_PESSOA'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=45))
    sobrenome = db.Column(db.String(length=45))
    data_nascimento = db.Column(db.String(length=45))
    naturalidade = db.Column(db.String(length=45))