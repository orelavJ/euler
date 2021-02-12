def factorial(n):
  if n == 1:
    return 1
  else:
    return n*factorial(n-1)

suma = 0
numero = str(factorial(100))

for digito in numero:
  suma += int(digito)
  
print(suma)
