"""
Exercício 9
#Escreva um programa que lê duas notas de vários alunos e armazena tais notas em um dicionário, onde a chave é o nome do aluno. 
# A entrada de dados deve terminar quando for lida uma string vazia como nome. Escreva uma função que retorna a média do aluno, dado seu nome.
"""

aluno = {}
lista = []
notas = ()


def calculaMedia (nome):
    notas = aluno.setdefault(nome_aluno)
    #print(len(notas))
    media = 0

    for i in range(len(notas)):
        media = media + notas[i]

    media = media / len(notas)

    return media


while True:
    nome_aluno = str(input("Informe o nome do Aluno (N para terminar): "))
    if nome_aluno == 'N':
        break
    numero_1 = float(input("Entre a primeira nota. "))  
    numero_2 = float(input("Entre a segunda nota. "))

    aluno.update({nome_aluno:(numero_1, numero_2)})
    #print(aluno)

print(aluno)


while True:
    nome_aluno = str(input("Informe o nome do Aluno: "))
    if nome_aluno in aluno:
        break

valor = calculaMedia(nome_aluno)

print(f"{nome_aluno} ficou com média {valor}.")

