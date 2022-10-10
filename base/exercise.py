from random import randint

nombres = [randint(1, 100) for x in range(1000)]

def plusPetit(nombres):
    jets = []
    for chiffre in nombres:
        if chiffre < 10:
            jets += [chiffre]
    return jets

print(plusPetit(nombres))

newNombres = [nombre for nombre in nombres if nombre < 10]

print(newNombres)