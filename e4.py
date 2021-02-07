#busca el palíndromo mas grande hecho a partir del producto
#de dos numeros de tres dígitos
list = []
for a in range(999, 101, -1):
  for b in range(999, 101, -1):
    x = str(a * b)
    if x == x[::-1] and len(x) == 6:
      list.append(x)
      break

print(max(list))
