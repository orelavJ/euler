#problem 15 lattice paths
#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?
endpoint = [20, 20]

def factorial(num):
  if num == 1:
    return 1
  return num*factorial(num-1)


def pathcount(endpoint):
  num = factorial(endpoint[0]+endpoint[1])

  den = (factorial(endpoint[0])*(factorial((endpoint[0]+endpoint[1])-endpoint[1])))
  return num//den
  
print(pathcount(endpoint))
