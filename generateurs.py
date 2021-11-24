import random
from time import time
from Generateur import *


def generateurExemple():
    """
    Exemple de suite
    """

    print("\n--- Exemple de suite ---")

    generateur = Generateur(seed=time(),
                            a=25214903617,
                            c=11,
                            m=281474976710656)
    generateur.genererSuite(1000)

    afficherInfos(generateur)


def generateurConstante():
    """
    Suite constante
    """

    print("\n--- Cas particulier: Suite constante ---")

    generateur = Generateur(seed=time(),
                            a=1, c=1, m=1)
    generateur.genererSuite(1000)

    afficherInfos(generateur)


def generateurIncrementNul():
    print("\n--- Cas particulier: Suite constante ---")

    generateur = Generateur(seed=time(),
                            a=65539, c=0, m=2147483648)

    generateur.genererSuite(1000)
    afficherInfos(generateur)


def generateurDeGenerateurMauvais():

    print("\n--- Générer une suite aléatoire ---")
    generateur = Generateur(seed=time(),
                            a=25214903617, c=11,
                            m=281474976710656)
    generateur.genererSuite(20)

    afficherInfos(generateur, showList=False)

    alea = Generateur(seed=time(),
                      a=65539, c=0,
                      m=2147483648)
    alea.genererSuite(10)

    afficherInfos(alea, showList=False)

    liste = construireListe(10, alea, generateur)

    print("\n")
    for i in liste:
        print(i)


def generateurDeGenerateur():
    print("\n--- Générer une suite aléatoire ---")
    generateur = Generateur(seed=time(),
                            a=25214903617, c=11,
                            m=281474976710656)
    generateur.genererSuite(10000)

    afficherInfos(generateur, showList=False)

    alea = Generateur(seed=time(),
                      a=65539, c=0,
                      m=2147483648)
    alea.genererSuite(10000)

    afficherInfos(alea, showList=False)

    liste = construireListe(10, alea, generateur)

    print("\n")
    for i in liste:
        print(i)

def construireListe(nb, a, b):
    liste = []
    for i in range(nb):
        index = int(a.suite[i % len(a.suite)]) % len(b.suite)
        liste.append(b.suite[index])

    return liste


def afficherInfos(generateur, nb=5, showList=True):
    generateur.info()

    if showList:
        generateur.afficherSuite(nb)
        generateur.afficherMoyenne()
