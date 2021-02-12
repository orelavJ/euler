import math
number = 220

pares = {}

def factorizar(n):
  factores = set()
  limite = math.sqrt(n)
  f = 2
  while n >= limite:
    if n % f == 0:
      factores.add(f)
      n = n//f
      f = f+1
    else:
      f = f+1
  return factores
  
def divisores(n):
  divisores = set()
  limite = n//2
  f = 2
  while f <= limite:
    if n % f == 0:
      divisores.add(f)
    f = f+1
  divisores.add(1)
  return divisores
n = 4
while n <= 10000:
  d = divisores(n)
  if len(d) != 0:
    pares[n] = sum(d)
  n = n+1
k = 4
total = 0
#print(pares)

while k <= 10000:
  try:
    for i in range(k+1, k+1000):
      if k == pares[i] and i == pares[k]:
        total = total+k+i

  except:
    k += 1
    continue
  k += 1
print(total)
