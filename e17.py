diccionario = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6}

suma = 0
number = 99

for i in range(1, 10):
  suma += diccionario[i]

unidades = suma

for i in range(10, 20):
  suma += diccionario[i]
  

for i in range(20, 100, 10):
  suma += 10*diccionario[i]
  suma += unidades

uno99 = suma

for i in range(1, 10):
  suma += diccionario[i]*100
  suma += 7
  suma += 10*99
  suma += uno99
  
print(suma+11)
