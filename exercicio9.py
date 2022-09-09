import math
import re


#equacao = str(input("Informe a equação do segundo grau para determinarmos suas raízes (ax^2+bx+c): "))  
equacao = r"1x^2-4x-25=0"

print(equacao)

#for posicao in equacao:
    #if posicao == 'x' or posicao == '=':
     #   if posicao + 1 == '^':
      #      a = equacao.split('x')
       #     print(a)
#    print(posicao)

padrao = 'x^2'
lista = re.split(padrao, equacao)
print(lista)

saida = re.

print(equacao.find('x^2'))

a = equacao[0:equacao.find('x^2')]
print(a)

aux = equacao[equacao.find('x^2')+3:]
print(aux)

if aux.find('x') == -1:
    b = 0
else:
    b = aux[0:aux.find('x')]

print(b)

bux = aux[aux.find('x')+1:]
print(bux)

if bux == '=0':
   c = 0
   print("Cheguei aqui")
else:
   c = bux[0:bux.find('=')]

print(c)

coefA = int(a)
coefB = int(b)
coefC = int(c)

print(f"Coeficientes - a:{coefA} b:{coefB} c:{coefC}")


# Tipo ax^2+c=0

if coefA == 0:
    print("Não é uma equação do 2º grau")
elif coefB == 0:
    if coefC > 0:
        print("Não possui raízes reais...")
    else:
        x1 = math.sqrt(-coefC/coefA)
        x2 = -x1
        print(f"As raízes são x1 = {x1} e x2 = {x2}")
elif coefC == 0:
    x1 = 0
    x2 = -coefB/coefA
    print(f"As raízes são x1 = {x1} e x2 = {x2}")
else:
    delta = (coefB**2)-4*coefA*coefC
    print(f"delta {delta}")
    if delta < 0:
        print("Não admite solução real...")
    else:
        x1 = (-coefB+math.sqrt(delta))/(2*coefA)
        x2 = (-coefB-math.sqrt(delta))/(2*coefA)
        print(f"As raízes são x1 = {x1} e x2 = {x2}")

#print(f"As raízes são x1 = {x1} e x2 = {x2}")




