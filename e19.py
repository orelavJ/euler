s = 1
sundays = 0

meses = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for a in range(1901, 2000):
  for m in range(1, 13):
    if s == 7:
      sundays += 1
    
    if a % 4 == 0 and m == 2:
      s += 1
    else:
      s += meses[m]-28
    if s > 7:
      s = s - 7

print(sundays)
