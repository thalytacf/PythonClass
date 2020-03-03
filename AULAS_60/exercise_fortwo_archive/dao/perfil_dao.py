from Hard.AulaX.model.perfil import Perfil

class PerfilDao:
    def __init__(self):
        self.arquivo = open('C:/Users/900163/Desktop/git/PythonHBSIS/Hard/AulaX/table.txt', 'r')

    def list_all(self):
        lista = []
        for p in self.arquivo:
            p = p.strip().split(';')
            model = Perfil(p[1], p[2], p[3], p[4], p[0])
            lista.append(model.__dict__)
        return lista

    def get_by_id(self,id):
        for p in self.arquivo:
            p = p.strip().split(';')
            model = Perfil(p[1], p[2], p[3], p[4], p[0])
            if id == int(p[0]):
                return model.__dict__



