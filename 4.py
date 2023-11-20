import random

l1 = [[int(random.normalvariate(50,20)) for x in range(random.randint(5,20))] for x in range(10)]

i = 0
for outerlist in l1:
  print(i, end=" ")
  # for element in outerlist:
  #   print(element, end=" ")
  for j in range(0,19):
    try:
      print(outerlist[j], end=" ")
    except:
      print( 0, end="  ")
  print()
  i = i + 1