dogs = ['mister', 'bulky', 'amber', 'penelope']
cats = ['Applebutter', 'Madam', 'Marigold', 'Goldensocks']

#swap lists

print(dogs)
print(cats)

import copy

dogsCopy=copy.copy(dogs)

for i in range(len(cats)):
    dogs.append(cats[i])
del dogs[:4]
print(dogs)

for i in range(len(dogsCopy)):
    cats.append(dogsCopy[i])
del cats[:4]
print(cats)

#randomly replace values between lists

import random as r
dogs.append(cats[r.randint(0, len(cats) - 1)])
print(dogs)
