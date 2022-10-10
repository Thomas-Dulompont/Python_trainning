nb1 = input('Premier Nombre :')
nb2 = input('Deuxieme Nombre :')
nb3 = input('Troisieme Nombre :')

if nb1 > nb2 and nb1 > nb3:
    print('Le nombre n°1({}) est le plus grand des trois'.format(nb1))
elif nb2 > nb3:
    print('Le nombre n°2({}) est le plus grand des trois'.format(nb2))
else:
    print('Le nombre n°3({}) est le plus grand des trois'.format(nb3))