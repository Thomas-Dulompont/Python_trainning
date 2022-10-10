
def ajouter_cle(var_lettre, var_cle, cond):
    """
    Fonction qui ajoute la clé ou la retirer selon la cond
    : param var_lettre (str) : Lettre à chiffrer / déchiffrer
    : param var_cle (int) : Clé utiliser lors du chiffrage
    : return (str) : Lettre chiffrée  / déchiffrée
    """
    if cond:
        lettre_chiffrer = chr(ord(var_lettre) - var_cle)
    else:
        lettre_chiffrer = chr(ord(var_lettre) + var_cle)
    return lettre_chiffrer

def chiffrer(var_texte, var_cles, cond):
    """
    Fonction qui chiffre ou déchiffre le texte donné
    : param var_texte (str) : Texte à chiffrer / déchiffrer
    : param var_cles (int) : Les Clés utiliser lors du chiffrage
    : return (str) : Texte chiffrée  / déchiffrée
    """
    texte_chiffrer = ""
    long_cles = len(var_cles) -1

    for lettre in var_texte:
        status_liste = 0
        if status_liste > long_cles:
            status_liste = 0
        else:
            texte_chiffrer += ajouter_cle(lettre, var_cles[status_liste], cond)
            status_liste += 1
    return texte_chiffrer

# Notre texte a chiffrer
clair = "Une petite phrase est un court extrait de discours ou une brève citation publique, d'acteurs sociaux"

# Les clés
cles = [6, 12, 10, 8]

# Notre texte chiffré
code = chiffrer(clair, cles, False)

# Notre texte déchiffré
uncode = chiffrer(code, cles, True)