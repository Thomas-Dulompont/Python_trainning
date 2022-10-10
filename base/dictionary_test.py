dictionnaire = {
    "test" : "test",
    "Chaussure" : "oui",
    "Oui" : "non"
}

mot = input("Entrer un mot à rechercher : ")

print(dictionnaire.get(mot, "Nous ne connaissons pas ce mot"))