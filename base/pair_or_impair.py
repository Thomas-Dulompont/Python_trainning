nombre = input('Quel nombre dois-je vérifier ?')
reponse = float(nombre) % 2.0
if reponse == 1:
    print('Ce nombre est impair')
else:
     print('Ce nombre est pair')
