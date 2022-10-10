
def multiplication(nb1, nb2):
    """
    Verifie et inverse un chiffre négatif et multiplie les deux nombres
    nb1(Int) : Premier nombre
    nb2(Int) : Deuxième nombre
    return(Int) : résultat de la multiplication
    """
    if nb1 < 0:
        nb1 = -nb1
    if nb2 < 0:
        nb2 = -nb2
    return nb1*nb2
