#halla la suma de los valores de la secuencia de fibonacci
#hasta 4 millones
l = [1, 2]
c = l[-1]+l[-2]
d = []
while c < 4000000:
  c = l[-1]+l[-2]
  l.append(c)
  print(l)
  if c % 2 == 0:
    d.append(c)
  else:
    continue
print(sum(d)+2)
