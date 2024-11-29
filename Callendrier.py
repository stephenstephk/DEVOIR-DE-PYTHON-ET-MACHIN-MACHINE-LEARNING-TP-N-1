# Fonction pour afficher un calendrier
def afficher_calendrier():
    # Vérification du nombre de jours dans le mois
    while True:
        jours_dans_mois = int(input("Entrez le nombre de jours dans le mois (entre 28 et 31) : "))
        if 28 <= jours_dans_mois <= 31:
            break  # Si le nombre est valide, on sort de la boucle
        print("Veuillez entrer un nombre entre 28 et 31 !")

    # Vérification du premier jour
    while True:
        premier_jour = int(input("Entrez le numéro du premier jour (1 pour Lundi,..., 7 pour Dimanche) : "))
        if 1 <= premier_jour <= 7:
            break  # Si le numéro est valide, on sort de la boucle
        print("Veuillez entrer un chiffre entre 1 et 7 !")

    # Affichage des en-têtes
    print("\nLUN MAR MER JEU VEN SAM DIM")

    # Espacement initial pour aligner le premier jour
    for _ in range(premier_jour - 1):
        print("    ", end="")

    # Affichage des jours du mois
    for jour in range(1, jours_dans_mois + 1):
        print(f"{jour:>3} ", end="")
        if (jour + premier_jour - 1) % 7 == 0:  # Retour à la ligne après dimanche
            print()

# Exécuter la fonction
afficher_calendrier()
