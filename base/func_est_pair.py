nb = int(input("Entrez un nombre entier : "))

def est_pair(nb):
    """
    Calcul le nombre entré par l'utilisateur pour connaître si il est Pair ou Impair
    : nb (Int) : Nombre entré par l'utilisateur
    : return (Bool) : True / False
    """
    estPair = True
    if nb % 2 == 0:
        estPair = True
    else:
        estPair = False
    return estPair

print(est_pair(nb))