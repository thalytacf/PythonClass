lista = []
dicionario = { 'chave':'valor', 'Nome':'Thalyta', 'Sobrenome':'Ficher'}

print (dicionario)
print (dicionario ['Sobrenome'])

nome = 'Thalyta'
listasnotas = [10,20,50,70]
media = sum(listasnotas)/len(listasnotas)
situacao = 'Resultado'
if media >= 7:
    situacao = 'Aprovado'

dicionario_alunos = {'Nome':nome, 'Lista_Notas':listasnotas, 'Media': media, 'Situacao': situacao}
print (f"{dicionario_alunos['Nome']}-{dicionario_alunos['Situacao']}")
