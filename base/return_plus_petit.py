nb1 = input('Premier Nombre :')
nb2 = input('Deuxieme Nombre :')
nb3 = input('Troisieme Nombre :')

def plus_petit(nb1, nb2, nb3):
    """
    Fonction qui prend pour argument 3 nombres, et renvoie le plus petit des trois
    nb1(Int) : Premier nombre
    nb2(Int) : Deuxième nombre
    nb3(Int) : Troisième nombre
    return : String
    """

    if nb1 > nb2 and nb1 > nb3:
        return nb1
    elif nb2 > nb3:
        return nb2
    else:
        return nb3

print(plus_petit(nb1, nb2, nb3))