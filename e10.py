import math

maximo = 2000000
limite = math.ceil(math.sqrt(maximo))
lista = [True]+[True]+[True]*maximo

for i in range(2, limite):
  if lista[i] == True:
    for j in range(i*i, maximo, i):
      lista[j] = False

t = 0

for v in range(2,maximo):
  if lista[v] == True:
    t = t+v
print(t)
