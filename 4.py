import random

l1 = [[int(random.normalvariate(50,20)) for x in range(random.randint(5,20))] for x in range(10)]

i = 0
for outerlist in l1:
  print(i, end=" ") #line
  for element in outerlist:
    print(element, end=" ") #nummer each
  
  #padding for 20 numbers
  try:
    #for x in range(20):
      if l1[19] == " ":
        print()
  except IndexError:
    for x in range(outerlist.index(element), 19):
      print(0, end=" ")
    #print("  " , outerlist.index(element)+1)
    print()

  #print()
  i = i + 1


  #richtig? -visuell nicht gleich lang