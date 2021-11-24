from generateurs import *


def main():

    titre = ["Exemple", "Constante", "Increment Nul",
             "Generateur Liste Aleatoire Mauvais",
             "Generateur Liste Aleatoire Bon", "Quitter"]
    actions = [generateurExemple, generateurConstante,
               generateurIncrementNul, generateurDeGenerateurMauvais,
               generateurDeGenerateur, quit]

    choix = range(len(titre))

    print("--- Menu - Congruentiel Linéaire ---")
    for i in choix:
        print(f'{choix[i]} - {titre[i]}')

    saisie = input("Choix :")

    if saisie.isnumeric():
        valeur = int(saisie)

        if valeur in choix:
            actions[valeur]()
            boucleMain()

    main()


def boucleMain():
    input("\nAppuyer sur entrée pour continuer...\n")
    main()


main()
