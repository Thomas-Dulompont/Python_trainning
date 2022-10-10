def moyenne(nb1, nb2, nb3):
    """
    Fait une moyenne de 3 nombres
    nb1(Int) : Premier nombre
    nb2(Int) : Deuxième nombre
    nb3(Int) : Troisème nombre
    return(Str) : Retourne le resultat
    """
    total = nb1 + nb2 + nb3
    resultat = total / 3

    return "La moyenne est de {}".format(round(resultat, 2))

print(moyenne(2,5,9))