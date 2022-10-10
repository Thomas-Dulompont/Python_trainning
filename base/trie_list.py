liste = [i for i in range(100)]
essais = 0

def recherche(chiffre, liste_triee, essais):
    if len(liste_triee) == 1:
        return "Premier chiffre de la liste"
    
    milieu = int(len(liste_triee) / 2)

    if liste_triee[milieu] == chiffre:
        print("Trouver en {} essais !".format(essais))
        return chiffre
    elif liste_triee[milieu] < chiffre:
        essais += 1
        return recherche(chiffre, liste_triee[milieu:], essais)
    else:
        essais += 1
        return recherche(chiffre, liste_triee[:milieu], essais)

print(recherche(55, liste, essais))