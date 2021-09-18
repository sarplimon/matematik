import random
lotterynubers = []
for i in range(0,6):
  for i in range (0,6):
    x= random.randint(1,49)
    while x in lotterynubers:
      x= random.randint(1,49)
    lotterynubers.append(x)
    lotterynubers.sort()
  print(lotterynubers)
  lotterynubers = []
  
