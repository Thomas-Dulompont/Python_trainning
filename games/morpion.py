import random


grille = {
"A" : ["-" , "-", "-"],
"B" : ["-" , "-" , "-"],
"C" : ["-" , "-" , "-"]
}

#VARIABLES GLOBALES

# Stock le nombre de tour
tour = 0

# Stock le dernier joueur
dernier_joueur = ""

# Stock le joueur en cours (On l'utilise pour l'ajouter aux messages)
joueur = ""

# Stock le symbole en cours
symbole = ""

#MESSAGES

message_egalite = "Egalité ! Personne n'a gagné cette fois ci ! "
message_gagnant = "Félicitation {} tu gagne la partie ! "
message_error = "Veuillez renseigner une case correct ! "
message_fill = "Cette case est déjà utilisé ! Veuillez en choisir une autre. "
message_play = "{} veuillez choisir une case : "
message_play_ordinateur = "L'ordinateur à choisit sa case : "
message_question_ordinateur = "Souhaitez vous jouer contre l'Ordinateur ? "


#FONCTIONS
def afficher_grille():
    """
    Fonction qui vérifie si l'on joue contre l'ordinateur pour afficher le Plateau seulement quand c'est notre tour de jouer
    """
    if dernier_joueur == "J1" and question_ordinateur.lower() == "oui":
        print("")
        print("")
        print(message_play_ordinateur)
        print("")
    else:
        print("")
        for element in grille:
            print(grille[element])
        print("")

def switch_joueur():
    """
    Fonction qui change le Joueur
    """
    if dernier_joueur == "J1":
        return "J2"
    else :
        return"J1"

def coup_ordinateur(grille):
    """
    Fonction qui génère une case pour l'ordinateur, qui se répéte si la case est utilisé
    : param grille : (dict) Plateau de Jeu
    """
    while True:
        cases = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        coup = str(cases[random.randint(0, 8)])
        ligne = coup[0]
        colonne = int(coup[1]) -1

        # Vérifie si la case générée est disponnible
        if grille["{}".format(ligne)][colonne] == "-":
            return coup

def verifier_gagant():
    """
    Fonction qui test toutes les possibilités et qui vérifie si les cases sont bien remplis
    """
    if grille["A"][0] == grille["A"][1] and grille["A"][0] == grille["A"][2] and grille["A"][0] != "-":
        return True
    if grille["B"][0] == grille["B"][1] and grille["B"][0] == grille["B"][2] and grille["B"][0] != "-":
        return True
    if grille["C"][0] == grille["C"][1] and grille["C"][0] == grille["C"][2] and grille["C"][0] != "-":
        return True
    if grille["A"][0] == grille["B"][0] and grille["A"][0] == grille["C"][0] and grille["A"][0] != "-":
        return True
    if grille["A"][1] == grille["B"][1] and grille["A"][1] == grille["C"][1] and grille["A"][1] != "-":
        return True
    if grille["A"][2] == grille["B"][2] and grille["A"][2] == grille["C"][2] and grille["A"][2] != "-":
        return True
    if grille["A"][0] == grille["B"][1] and grille["A"][0] == grille["C"][2] and grille["A"][0] != "-":
        return True
    if grille["A"][2] == grille["B"][1] and grille["A"][2] == grille["C"][0] and grille["A"][2] != "-":
        return True

# Message unique envoyé à l'utilisateur pour savoir si il souhaite jouer contre l'ordinateur
question_ordinateur = input(message_question_ordinateur)

# Début du Jeu
while True:

    # Affiche la grille
    afficher_grille()

    # Vérifie si l'on est contre l'ordinateur pour éviter de nous faire jouer même quand c'est pas notre tour
    if question_ordinateur.lower() == "oui":
        if dernier_joueur == "J1":
            symbole = "O"
            joueur = "Ordinateur"

            # Input de l'ordinateur
            son_choix = coup_ordinateur(grille)
        else:
            symbole = "X"
            joueur = "Joueur n°1"

            # Input du Joueur contre l'ordinateur
            son_choix = input(message_play.format(joueur))
    else:
        if dernier_joueur == "J1":
            symbole = "O"
            joueur = "Joueur n°2"
        else:
            symbole = "X"
            joueur = "Joueur n°1"
        
        # Input Joueur contre Joueur
        son_choix = input(message_play.format(joueur))

    # On transforme les caractères entrer par l'utilisateur en majuscule
    son_choix = son_choix.upper()

    # On regarde la longueur des caractères entrer par l'utilisateur
    if len(son_choix) > 2 or len(son_choix) < 2:
        print(message_error)
    # On vérifie que l'utilisateur n'a pas entrer autre chose (2e caractère)
    elif son_choix[1] != "1" and son_choix[1] != "2" and son_choix[1] != "3":
        print(message_error)
    # On vérifie que le chiffre entrer n'est pas plus grand que 3
    elif int(son_choix[1]) > 3:
        print(message_error)
    # On regarde si le premier caractère est sois A, B ou C
    elif son_choix[0] == "A":
        if grille["A"][int(son_choix[1]) -1] == "-":
            grille["A"][int(son_choix[1]) -1] = symbole
            tour += 1
            dernier_joueur = switch_joueur()
        else:
            print(message_fill)
    elif son_choix[0] == "B":
        if grille["B"][int(son_choix[1]) -1] == "-":
            grille["B"][int(son_choix[1]) -1] = symbole
            tour += 1
            dernier_joueur = switch_joueur()
        else:
            print(message_fill)
    elif son_choix[0] == "C":
        if grille["C"][int(son_choix[1]) -1] == "-":
            grille["C"][int(son_choix[1]) -1] = symbole
            tour += 1
            dernier_joueur = switch_joueur()
        else:
            print(message_fill)
    # Si toutes nos vérifications ne sont pas passer on met un message d'erreur
    else:
        print(message_error)

    # On commence à vérifier la victoire au bout de 5 tours
    if tour >= 5:
        if verifier_gagant():
            print("")
            print(message_gagnant.format(joueur))
            print("")
            for element in grille:
                print(grille[element])
            break
    # Au bout de 9 tours on sait que le match est nul
    elif tour == 9:
        print("")
        print(message_egalite)
        print("")
        break