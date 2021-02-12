valores = {}

nombres = {}

def ordenar(A):
  i = 1
  j = i-1
  while i <= len(A)-1:
    pick = A[i]
    while A[j] > pick and j >= 0:
      A[j+1] = A[j]
      A[j] = pick
      j = j-1
    j = i
    i = i+1
    
  return A

f = open("p022_names.txt", "r")
A = ""
for l in f:
  A += l

A = A.replace('"', '').split(",")

A = ordenar(A)

for i in range(65, 91):
  valores[chr(i)] = i-64

tmp = 0
for n in A:
  for c in n:
    tmp += ord(c)-64
  nombres[n] = tmp
  tmp = 0


i = 1
for nombre in nombres:
  tmp += i*nombres[nombre]
  i = i+1
print(tmp)
