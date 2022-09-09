"""
Exercício 10
#Escreva um programa para armazenar uma agenda de telefones usando um dicionário. Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o nome completo da pessoa. Seu programa deve ter as seguintes funções:
­a) incluir_novo_nome – essa função acrescenta um novo nome na agenda, com um ou mais telefones. Ela deve receber como argumentos o nome e os telefones.
b) incluir_telefone – essa função acrescenta um telefone em um nome existente na agenda. Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja incluí-­lo. Caso a resposta seja afirmativa, use a função anterior para incluir o novo nome. ­ 
c) excluir_telefone – essa função exclui um telefone de uma pessoa que já está na agenda. Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda.
d) excluir_nome – essa função exclui uma pessoa da agenda.
e) consultar_telefone – essa função retorna os telefones de uma pessoa na agenda.

"""
import collections

contatos = {}
notas = ()


def incluiContato():
    telefones = []
    nomeCont = str(input("Informe o nome do Contato: "))
    numTel = str(input("Informe o número de telefone (DDD) + tel: "))
    telefones.append(numTel)  
   
    contatos.update({nomeCont:telefones})
    
    print(contatos)

def incluiContatoAvancado(nomeCont,*nrosTels):
    telefones = []

    if len(nrosTels) == 0:
        numTel = str(input("Informe o número de telefone (DDD) + tel: "))
        telefones.append(numTel)
    else:
        for i in range(len(nrosTels)):
            telefones.append(nrosTels[i])  
   
    contatos.update({nomeCont:telefones})
    
    print(contatos)


def incluiTelefone(nomeCont):
    if nomeCont in contatos:
        print(f"Encontrado {nomeCont} como contato na agenda.")
        numTel = str(input("Informe o número de telefone (DDD) + tel: "))
        contatos.setdefault(nomeCont).append(numTel)
        print(contatos)
    else:
        opcao = str(input(f"Contato não encontrado na Agenda! Deseja incluí-lo? (Digite S para Sim ou N para Não): "))
        if opcao == 'S' or opcao == 's':
            incluiContatoAvancado(nomeCont)
        
def consultaContato(nomeCont):
    print(contatos.setdefault(nomeCont))

def excluiContato(nomeCont):
    contatos.pop(nomeCont)
    print(f"Contato excluído.")
    print(contatos)

def excluiTelefone(numTel):
    agenda = contatos.copy()
    listaAux = []
    numUnico = 0
    for contato in agenda:
        #print(f"{user} - {contatos.get(user)}")
        for tel in agenda.get(contato):
            if tel == numTel:
                if len(agenda.get(contato)) > 1:
                    print(f"{contato} - {tel} - {len(agenda.get(contato))}")
                    contatos.get(contato).remove(tel)
                    print(f"Número excluído.")
                    
                else:
                    print(f"{contato} - {tel} - {len(agenda.get(contato))}")
                    excluiContato(contato)
                    #numUnico = 1
                    #listaAux.append(contato)

    #if numUnico == 1:
     #    for i in range(len(listaAux)):
      #      excluiContato(listaAux[i])  

    print(contatos)
        
    #lista = contatos.items()
    #print(lista)
    #print(type(lista))
    #print(contatos)

def ordenaContato(): #Gera uma lista de tuplas
    result = collections.OrderedDict(sorted(contatos.items()))
    print(result)
    
   
incluiContatoAvancado('Ione', '051984010101', '05132598888', '05140040100')
incluiContatoAvancado('Aline', '051991067875')
incluiContatoAvancado('Carlos', '051991957516', '05133409628')
incluiContatoAvancado('Elci', '05133409628')

excluiTelefone('05133409628')
excluiTelefone('05140040100')
excluiTelefone('051991957516')

incluiContatoAvancado('Rafael', '051991957516', '05133409628')
ordenaContato()

"""
incluiContato()
incluiContato()
incluiContatoAvancado('Ione', '051984010101', '05132598888', '05140040100')
incluiTelefone('Carlos')
incluiTelefone('Elci')
consultaContato('Aline')
excluiContato('Aline')
excluiTelefone('05140040100')

"""