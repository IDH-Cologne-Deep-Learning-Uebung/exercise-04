import random

l1 = [[int(random.normalvariate(50, 20)) for x in range(random.randint(5, 20))] for x in range(10)]

i = 0
for outerlist in l1:
    print(i, end=" ")
    for element in outerlist:
        print(element, end=" ")
    print()
    i = i + 1

for row, outerlist in enumerate(l1):
    print(row, end=' ')
    for col in range(20):  # Adjust the range as needed
        try:
            value = outerlist[col]
            print(value, end=' ')
        except IndexError:
            print(0, end=' ')
    print()