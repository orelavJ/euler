#el menor numero positivo divisible entre 20!
n = 2520 #2520 es divisible entre 10!
i = [11, 13, 14, 16, 17, 18, 19, 20]
k = 0
while k < 7:
  if n % i[k] == 0:
    k += 1
  else:
    n += 2520
    k = 0
		
print(n)
