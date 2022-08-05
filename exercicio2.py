import sys

lista = []
lista_aux = []
#print(lista)

i = int()

while True:
    i = int(input("Digite um valor inteiro (-1 para terminar): "))
    if i == -1:
        break
    lista.append(i)

print(f"A lista possui {len(lista)} elementos, são eles: ", lista)

x = len(lista) - 1

while x >= 0 :
    lista_aux.append(lista[x])
    x = x - 1
print(f"Os elementos da lista dispostos de forma invertida: ", lista_aux)

x = 0
valor = 0
while x < len(lista):
    valor = valor + lista[x]
    #print(f"A soma parcial é: {valor} ")
    x = x + 1
print(f"A soma total é: {valor} ")

media = valor / len(lista)
print(f"A média é: {media} ")

x = 0
lista_aux = []
#print(lista_aux)
for i in range(len(lista)):
    if media < lista[i]:
        lista_aux.append(lista[i])
        x = x + 1
print(f"A lista possui {len(lista_aux)} elementos acima da média, são eles: ", lista_aux)

x = 0
lista_aux = []
#print(lista_aux)

for i in range(len(lista)):
    if lista[i] < 7:
        lista_aux.append(lista[x])
        x = x + 1
print(f"A lista possui {len(lista_aux)} elementos abaixo de 7, são eles: ", lista_aux)

try:
    sys.exit("Programa finalizado...")
except SystemExit:
    print('Programa finalizado com a exceção SystemExit')