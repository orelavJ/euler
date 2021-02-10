triangulo = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


nodos = len(triangulo.replace("\n", "").split(" "))

triangulo = triangulo.split("\n")
for i in range(len(triangulo)):
  triangulo[i] = triangulo[i].split(" ")
  for ii in range(0, len(triangulo[i])):
    triangulo[i][ii] = int(triangulo[i][ii])


grafo = {}
for nodo in range(0, nodos):
  grafo[nodo] = {}

for n in range(len(triangulo)-1, -1, -1):
  for i in range(0, n):
    if triangulo[n][i] > triangulo[n][i+1]:
      triangulo[n-1][i] += triangulo[n][i]
      num_nodo = ((n+1)*(n))//2
      num_nodo += i
      num_nodo_padre = num_nodo - n
      grafo[num_nodo_padre]["v"] = num_nodo
    else:
      triangulo[n-1][i] += triangulo[n][i+1]
      num_nodo = ((n+1)*(n))//2
      num_nodo += i+1
      num_nodo_padre = num_nodo - n - 1
      grafo[num_nodo_padre]["v"] = num_nodo
    
pasos = [0]
def getpath(inicio, lista):
  try:
    hijo = inicio['v']
    lista.append(hijo)
    hijo = grafo[hijo]
    return getpath(hijo, lista)
  except:
    return lista

getpath(grafo[0], pasos)

print("La suma máxima de números adyacentes en el triángulo es:", triangulo[0])
print("El recorrido es:", pasos)
