
from Hard.Aula60.reolução2.local import Local

class Aviao(Local):
    def __init__(self):
        pessoas = []
        super().__init__(pessoas)

    def __str__(self):
        return 'Avião'