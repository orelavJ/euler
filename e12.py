import math

def nuevoTriangulo2(k):
  triangulo = (k*(k+1))//2
  return triangulo

def factores2(k):
  A = set()
  n = 1
  k = k
  triangulo = nuevoTriangulo2(k)
 # print(triangulo)
  while n < math.sqrt(triangulo):
    if triangulo % n == 0:
        A.add(triangulo//n)
        A.add(n)
    n = n+1
 # print(triangulo)
  return [len(A), triangulo]
#o = 0

#while True:
#  if factores(o)[0] > 500:
#    print(factores(o)[1])
#    break
#  else:
#    o += 1



