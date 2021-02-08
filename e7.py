import math


def criba(limite):
  cnt = 0
  nmb = 0
  L = [0]+[0]+[1]+[1]*(limite-1)
  for i in range(2, math.ceil(math.sqrt(limite))):
    if L[i] == 1:
      for j in range(i*2, limite+2, i):
        L[j] = 0

  for v in L:
    if v == 1:
      cnt = cnt+1
    nmb = nmb+1
    if cnt == 10001:
      break
  if cnt < 10001:
    return cnt
  else:
    print("El número:", nmb-1, "es el primo número:", cnt)
    return cnt
    
    
limite = 10000

while criba(limite)<10001:
  limite = limite+5000
  print(limite)

