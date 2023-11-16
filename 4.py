import random

l1 = [[int(random.normalvariate(50,20)) for x in range(random.randint(5,20))] for x in range(10)]

longestList= 0
# calculate longest list
for j in l1:
  if len(j) > longestList:
    longestList = len(j)


i = 0
for outerlist in l1:
  print(i, end=" ")
  if len(outerlist) < longestList:
    diff= longestList - len(outerlist)
    for x in range(0,diff):
      outerlist.append("00")


  for element in outerlist:
    print(element, end=" ")
  print()
  i = i + 1