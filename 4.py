import random

l1 = [[int(random.normalvariate(50,20)) for x in range(random.randint(5,20))] for x in range(10)]

i = 0
for outerlist in l1:
  print(i, end=" ")
  for element in outerlist:
    print(element, end=" ")
  print()
  i = i + 1

# Iterating over rows
for i, outerlist in enumerate(l1):
    # Print the row number
    print(i, end=" ")

    # Iterating over elements in the current row
    for element in outerlist:
        # Print each element
        print(element, end=" ")

    # Padding with zeros to reach the length of 20
    for j in range(len(outerlist), 20):
        print(0, end=" ")

    # Move to the next line
    print()
