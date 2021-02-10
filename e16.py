exp = 1000
numero = 2**exp
digitos = 0

while numero > 1:
  numero = numero//10
  digitos += 1

numero = 2**exp
num = 0
for i in range(digitos, -1, -1):

  tmp_num = numero//(10**i)
  numero -= tmp_num*10**i
  num += tmp_num

print(num)
