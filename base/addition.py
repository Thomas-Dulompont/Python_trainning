#nombres = [10,54,65,97,876,98]

def addition(nombres):
    """
    Donne la somme des nombres entrés
    : param nombres (List) : Liste de nombres
    : return (float) : Total
    """
    total = 0
    for chiffre in nombres:
        total += chiffre

    return total

print(addition([10,54,65,97,876,6789]))
