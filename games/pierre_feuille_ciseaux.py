import random

signes = ["Pierre", "Feuille", "Ciseaux"]

ordinateur = signes[random.randint(0, 2)]

winMessage = "Ordinateur : {}. Gagné ! Vous avez battu l'ordinateur !".format(ordinateur)
loseMessage = "Ordinateur : {}. Perdu ! Vous pouvez rejouer !".format(ordinateur)
egalityMessage = "Ordinateur : {}. Egalité ! Vous pouvez rejouer !".format(ordinateur)

print("Choisis un signe :")
print("1 - Pierre")
print("2 - Feuille")
print("3 - Ciseaux")

while True : 
    choix = int(input("Choisis un signe :"))
    if choix == 1 :
            if ordinateur == signes[0]:
                print(egalityMessage)
                break
            if ordinateur == signes[1]:
                print(loseMessage)
                break
            if ordinateur == signes[2]:
                print(winMessage)
                break
    if choix == 2 :
            if ordinateur == signes[0]:
                print(winMessage)
                break
            if ordinateur == signes[1]:
                print(egalityMessage)
                break
            if ordinateur == signes[2]:
                print(loseMessage)
                break
    if choix == 3 :
            if ordinateur == signes[0]:
                print(loseMessage)
                break
            if ordinateur == signes[1]:
                print(winMessage)
                break
            if ordinateur == signes[2]:
                print(egalityMessage)
                break
    else :
        print(" ")
        print("/!\ Le signe choisit ne fait pas partit du jeu... Recommence avec un signe correct !")
        print(" ")
