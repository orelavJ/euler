#Terna pitagórica
#a²+b²=c²
#a<b<c
#a+b+c=1000
#primitivo
#a*b*c=?
# m>n>0
#a = m²-n²
#b = 2*m*n
#c = m²+n²
import math

suma = 1000

for i in range(2, math.ceil(math.sqrt(suma/2))):
  if suma/2 % i == 0:
    if i % 2 == 0:
      for k in range(1, i-1, 2):
        if (2*i*i)+(2*i*k) == 1000:
          m = i
          n = k
    if i % 3 == 0:
      for k in range(2, i-1, 2):
        if (2*i*i)+(2*i*k) == 1000:
          m = i
          n = k

print("A: ", (m**2)-(n**2),"\nB: ", (2*m*n), "\nC: ", (m*m)+(n*n),"\nabc = ", ((m*m)-(n*n))*(2*m*n)*((m*m)+(n*n)))
