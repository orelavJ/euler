#The following iterative sequence is defined for the set of positive integers:

#n → n/2 (n is even)
#n → 3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

#Which starting number, under one million, produces the longest chain?

collatz = {}
collatz[10] = 5
starter = 2
number = 0
cycle = 0
tmp_cycle = 0
longest_cycle_number = 0

while starter < 999999:
  number = starter
  tmp_cycle = 0
  while number > 1:
    if number in collatz:
      tmp_cycle += collatz[number]
      break
    if number % 2 == 0:
      number = number/2
    else:
      number = (3*number)+1
    tmp_cycle += 1
  collatz[starter] = tmp_cycle
  if tmp_cycle > cycle:
    cycle = tmp_cycle
    longest_cycle_number = starter
  starter = starter + 1

print(cycle, longest_cycle_number)



