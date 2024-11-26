def afficher_calendrier(nombre_jours, premier_jour):
    jours_semaine = ["LUN", "MAR", "MER", "JEU", "VEN", "SAM", "DIM"]

    # Afficher les en-têtes des jours
    print(" ".join(jours_semaine))

    # Calculer l'indentation pour le premier jour
    indentation = (premier_jour - 1) * 4  # Chaque jour prend 4 espaces
    print(" " * indentation, end="")

    # Afficher les jours du mois
    for jour in range(1, nombre_jours + 1):
        print(f"{jour:>3} ", end="")  # Chaque jour est aligné à droite sur 3 caractères
        if (jour + premier_jour - 1) % 7 == 0:  # Passer à la ligne après DIM
            print()

# Entrée utilisateur
if __name__ == "__main__":
    print("Bienvenue dans le programme de calendrier !")
    nombre_jours = int(input("Entrez le nombre de jours dans le mois : "))
    premier_jour = int(input("Entrez le numéro du premier jour (1=LUN, 2=MAR, ..., 7=DIM) : "))

    # Validation des entrées
    if 28 <= nombre_jours <= 31 and 1 <= premier_jour <= 7:
        afficher_calendrier(nombre_jours, premier_jour)
    else:
        print("Entrées invalides. Assurez-vous que le nombre de jours est entre 28 et 31 et que le premier jour est entre 1 et 7.")
