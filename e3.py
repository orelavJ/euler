#halla el divisor primo más grande de n
n = 600851475143
list = []
d = 1
product = 1
k = 0

while product != n:
  d += 1
  if n % d == 0 and d != 1:
    list.append(d)
    product *= list[k]
    k += 1

print(list)
