
def chiffrement(var_clair, var_cle):
    """
    Fonction qui chiffre le texte donné en fonction de la clé donné
    : param var_clair (str) : Lettre à chiffrer
    : param var_cle (int) : Clé utiliser lors du chiffrage
    : return (str) : Lettre chiffrée 
    """
    chiffrer = ""
    for lettre in var_clair:
        chiffrer += chr(ord(lettre) + var_cle)
    return chiffrer

def dechiffrement(var_code, var_cle):
    """
    Fonction qui déchiffre le texte donné en fonction de la clé donné
    : param var_clair (str) : Lettre à déchiffrer
    : param var_cle (int) : Clé utiliser lors du déchiffrage
    : return (str) : Lettre déchiffrée 
    """
    dechiffrer = ""
    for lettre in var_code:
        dechiffrer += chr(ord(lettre) - var_cle)
    return dechiffrer

def analyse_frequence(var_code):
    """
    Fonction qui analyse et stock la fréquence des caractères dans le texte donné
    : param var_code (str) : Code à analyser 
    : return (dict) : Lettres triées
    """
    caracteres = {}
    for lettre in var_code:
        if lettre in caracteres: 
            caracteres[lettre] += 1
        else:
            caracteres[lettre] = 1

    caracteres_trier = dict(sorted(caracteres.items(), key=lambda item:item[1], reverse=True))
    return caracteres_trier

def trouver_cle(var_code):
    """
    Fonction qui détermine la clé utiliser lors du chiffrage selon le nombre d'apparition du caractère " " (espace) et envoie un message si elle est trouvée
    : param var_code (str) : Code à analyser
    """
    first_caracteres_trier = ord(list(analyse_frequence(var_code).keys())[0])
    espace_chiffre = ord(" ")

    if first_caracteres_trier >= espace_chiffre:
        decode = first_caracteres_trier - espace_chiffre
    else:
        decode = espace_chiffre - first_caracteres_trier
    print("Le texte décoder est : ")
    print(dechiffrement(var_code, decode))
    print("La Clé utilisé est : {}".format(decode))

# Notre texte a chiffrer
clair = "Une petite phrase est un court extrait de discours ou une brève citation publique, d'acteurs sociaux"

# Notre clé
cle = 1

# Notre texte chiffré
code = chiffrement(clair, cle)

# Notre texte déchiffré
uncode = dechiffrement(code, cle)

# Notre code qui va nous servir à trouver la clé
craquer = trouver_cle(code)