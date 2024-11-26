import random  # Importer la bibliothèque random pour choisir des régions au hasard

# Base de données simple : régions et leurs chefs-lieux
regions = regions_ci = {
    "Abidjan": "Abidjan",
    "Yamoussoukro": "Yamoussoukro",
    "Grands-Ponts": "Dabou",
    "La Mé": "Adzopé",
    "Agneby-Tiassa": "Agboville",
    "Cavally": "Guiglo",
    "Guémon": "Duékoué",
    "Tonkpi": "Man",
    "Gbôklé": "Sassandra",
    "Nawa": "Soubré",
    "San-Pédro": "San-Pédro",
    "Gôh": "Gagnoa",
    "Lôh-Djiboua": "Divo",
    "Haut-Sassandra": "Daloa",
    "Marahoué": "Bouaflé",
    "Gbêkê": "Bouaké",
    "Hambol": "Katiola",
    "Bafing": "Touba",
    "Béré": "Mankono",
    "Worodougou": "Séguéla",
    "Bagoué": "Boundiali",
    "Poro": "Korhogo",
    "Tchologo": "Ferkessédougou",
    "Bounkani": "Bouna",
    "Gontougo": "Bondoukou",
    "Indénié-Djuablin": "Abengourou",
    "Sud-Comoé": "Aboisso",
    "Belier": "Toumodi",
    "Iffou": "Daoukro",
    "Moronou": "Bongouanou",
    "Folon": "Minignan",
    "Kabadougou": "Odienné"
}

# Fonction pour jouer une partie
def jouer_partie():
    print("Bienvenue au jeu des régions et chefs-lieux de Côte d'Ivoire !")

    # Afficher les meilleurs scores fictifs
    meilleurs_scores = [80, 75, 70, 60, 50]
    print("Les 5 meilleurs scores :")
    print(", ".join(map(str, meilleurs_scores)))

    # Liste pour garder les questions déjà posées
    questions_posees = []
    score = 0  # Initialiser le score à 0

    # Poser 10 questions
    for i in range(10):
        # Choisir une région au hasard parmi celles qui n'ont pas encore été posées
        region, chef_lieu = random.choice(list(regions.items()))
        while region in questions_posees:
            region, chef_lieu = random.choice(list(regions.items()))
        questions_posees.append(region)  # Marquer cette région comme déjà posée

        # Poser la question à l'utilisateur
        print(f"\nQuestion {i+1}: Quel est le chef-lieu de la région {region} ?")
        reponse = input("Votre réponse : ")

        # Vérifier si la réponse est correcte
        if reponse.strip().lower() == chef_lieu.lower():
            print("Bonne réponse !")
            score += 10  # Ajouter 10 points pour une bonne réponse
        else:
            print(f"Mauvaise réponse. La bonne réponse est : {chef_lieu}")

    # Afficher le score final à la fin de la partie
    print(f"\nPartie terminée ! Votre score final est de : {score}/100")

# Programme principal
if __name__ == "__main__":
    # Lancer une partie
    jouer_partie()
