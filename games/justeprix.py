import random

prix =  random.randint(1, 10)

essais = 0

print("Devine le juste prix entre 1 & 10 !")

while True:
    nombre = int(input())
    essais += 1
    if nombre < prix :
        print("C'est plus")
    if nombre > prix :
        print("C'est moins")
    if nombre == prix :
        print("Vous avez trouvé le juste prix qui était {} en {} essais !".format(prix,essais))
        print("Fin de partie !")
        break