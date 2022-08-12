#alunos = dict(nome, nota1, nota2)
aluno = {}
lista = []
notas = ()

while True:
    nome_aluno = str(input("Informe o nome do Aluno (N para terminar): "))
    if nome_aluno == 'N':
        break
    numero_1 = float(input("Entre a primeira nota. "))  
    numero_2 = float(input("Entre a segunda nota. "))

    aluno.update({nome_aluno:(numero_1, numero_2)})
    #aluno.update({'nome':nome_aluno, 'nota1':numero_1, 'nota2':numero_2})
    print(aluno)
    #lista.append(aluno)

print(aluno)

nome_aluno = str(input("Informe o nome do Aluno: "))

print(aluno.keys())
print(aluno.values())
print(aluno.setdefault(nome_aluno))
print(type(aluno.setdefault(nome_aluno)))

notas = aluno.setdefault(nome_aluno)
print(len(notas))

media = 0

for i in range(len(notas)):
        media = media + notas[i]

media = media / len(notas)

print(f"{nome_aluno} ficou com média {media}.")

