

lista1 = [] 
lista2 = [] 
lista_aux = []


valor = int()

for i in range(10):
     valor = int(input("Digite um valor inteiro a ser inserido na Lista 1: "))
     lista1.append(valor)

for i in range(10):
     valor = int(input("Digite um valor inteiro a ser inserido na Lista 2: "))
     lista2.append(valor)

print(f"A lista 1 possui {len(lista1)} elementos, são eles: ", lista1)
print(f"A lista 2 possui {len(lista2)} elementos, são eles: ", lista2)

for i in range(len(lista1)):
    lista_aux.append(lista1[i])
    lista_aux.append(lista2[i])

#lista_aux = lista1[:]
#lista_aux.extend(lista2)

print(f"A lista gerada possui {len(lista_aux)} elementos, são eles: ", lista_aux)

