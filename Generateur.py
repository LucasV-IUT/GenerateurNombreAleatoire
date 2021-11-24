class Generateur():

    def __init__(self, seed, a, c, m):
        """

        :param seed: Germe de la suite (X0)
        :param a: Le multiplicateur de la fonction
        :param c: L'incrément de la fonction
        :param m: Modulo
        """

        # Graine et definition du premier élément de la suite
        self.seed = seed
        self.Xi = seed
        self.suite = []

        # Définition des paramètres de la suite
        self.a = a
        self.c = c
        self.m = m

    def info(self):
        """
        Affiche les paramètres initiaux de la fonction
        """
        print(f'a={self.a} ; c={self.c} ; m={self.m}')
        print(f"seed = {self.seed}\n")

    def calculer(self):
        """
        Calcule un nouveau nombre a partir du précédent
        :return: (a * Xi + c) % m
        """

        self.Xi = (self.Xi * self.a + self.c) % self.m
        return self.Xi

    def genererSuite(self, n):
        """
        Calcule n fois la suite
        :param n: Nombre de fois où l'on calcule la suite
        """

        for i in range(1, n):
            self.suite.append(self.calculer())

    def afficherSuite(self, nPremiers):
        """
        Affiche les n premiers elements de la suite
        :param nPremiers: nombre d'éléments de la suite a afficher
        """

        for i in range(nPremiers):
            print(f"X{i+1} = {self.suite[i]}")

    def moyenne(self):
        """
        :return: La moyenne de la suite
        """
        moyenne = 0
        nbElt = len(self.suite)
        for i in range(nbElt):
            moyenne += self.suite[i]

        moyenne /= nbElt

        return moyenne

    def afficherMoyenne(self):
        """
        Affiche la moyenne
        """
        print(f"\nMoyenne: {self.moyenne()}")
