from Hard.Aula55.dao.base_dao import BaseDao
from Hard.Aula55.model.pessoa_model import Pessoa

class PessoaDao(BaseDao):
    def __init__(self):
        super().__init__(Pessoa)