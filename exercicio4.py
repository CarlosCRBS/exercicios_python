#alunos = dict(nome, nota1, nota2)
aluno = {}
lista = []

while True:
    nome_aluno = str(input("Informe o nome do Aluno (N para terminar): "))
    if nome_aluno == 'N':
        break
    numero_1 = float(input("Entre a primeira nota. "))  
    numero_2 = float(input("Entre a segunda nota. "))

    aluno = dict(nome=nome_aluno, nota1=numero_1, nota2=numero_2)
    #aluno.update({'nome':nome_aluno, 'nota1':numero_1, 'nota2':numero_2})
    print(aluno)
    lista.append(aluno)

print(lista)

for i in range(len(lista)):
    media = (lista[i].get('nota1') + lista[i].get('nota2'))/2
    if media >= 7:
        lista[i].update({'situacao':'APROVADO'})
    else: lista[i].update({'situacao':'REPROVADO'})
    
print(lista)
    
nome_aluno = str(input("Informe o nome do Aluno: "))

for i in range(len(lista)):
    if lista[i].get('nome') == nome_aluno:
        media = (lista[i].get('nota1') + lista[i].get('nota2'))/2
        print(f"{nome_aluno} ficou com média {media}.")
    
    