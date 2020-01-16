from endereco_db import listar_todos
from endereco_converte import converter_tabela_dicionario
from endereco_exportar import exportar_txt


let = listar_todos()
led = converter_tabela_dicionario(let)
exportar_txt(led)