i = 0
k = 0
a = []
while i < 1000:
  if i % 3 == 0 or i % 5 == 0:
    a.append(i)
    k += i
    i += 1
  else:
    i += 1
	
print(a)
print(k)
