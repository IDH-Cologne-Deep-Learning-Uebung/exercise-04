import random

l1 = [[int(random.normalvariate(50,20)) for x in range(random.randint(5,20))] for x in range(10)]

i = 0
for outerlist in l1:
  print(i, end=" ")
  for element in outerlist:
    print(element, end=" ")
  print()
  i = i + 1

for outerlist in l1:
    k = 0
    while k < 19:
        try: outerlist[k]
        except: outerlist.append(0)
        k = k + 1

print('\n\n')

for outerlist in l1:
        print(i, end=" ")
        for element in outerlist:
            print(element, end=" ")
        print()
        i = i + 1