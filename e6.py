#encuentra la diferencia entre la suma de los cuadrados
#de los cien primeros numeros naturales y el cuadrado de la suma
n = 1
s = 0

for i in range(1, 101):
  s += n * n
  n += 1

j = sum(list(range(1, 101)))

print((j*j) - s)
