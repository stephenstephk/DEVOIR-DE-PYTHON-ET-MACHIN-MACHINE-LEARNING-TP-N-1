#import de la bliotheque random pour les chois aleatoire des regions
import random

# Dictionnaire des regions et leur chef lieu
regions = {
    "Agnéby-Tiassa": "Agboville",
    "Bafing": "Touba",
    "Bagoué": "Boundiali",
    "Belier": "Yamoussoukro",
    "Bere": "Mankono",
    "Bounkani": "Bouna",
    "Cavally": "Guiglo",
    "Folon": "Minignan",
    "Gbeke": "Bouaké",
    "Gôh": "Gagnoa",
    "Gontougo": "Bondoukou",
    "Grands-Ponts": "Dabou",
    "Guemon": "Duékoué",
    "Hambol": "Katiola",
    "Haut-Sassandra": "Daloa",
    "Iffou": "Daoukro",
    "Indénié-Djuablin": "Abengourou",
    "Kabadougou": "Odienné",
    "Lôh-Djiboua": "Divo",
    "La Mé": "Adzopé",
    "Marahoué": "Bouaflé",
    "Moronou": "Bongouanou",
    "Nawa": "Soubré",
    "N'Zi": "Dimbokro",
    "Poro": "Korhogo",
    "San-Pedro": "San-Pédro",
    "Sud-Comoé": "Aboisso",
    "Tchologo": "Ferkessédougou",
    "Tonkpi": "Man",
    "Worodougou": "Séguéla",
    "Yamoussoukro": "Yamoussoukro"
}

# Liste pour recuperer les meilleurs scores
meilleurs_scores = [0.0,0.0,0.0,0.0,0.0]

# Fonction pour jouer 
def jouer():
    Note = 0
    Score = 0.0
    questions_posees = set()
    Pseudo = input("Quel est votre Pseudo ?  ")
    print("\n*** Les 5 meilleurs scores ***")
    for i, sc in enumerate(sorted(meilleurs_scores, reverse=True)[:5]): # reverse = True pour trier par ordre decroissant et donc avoir de plus gransd au plus petit dans la liste
        print(f"{i + 1}. {sc} points")
    
    print("\n*** DEBUT DU JEU ***")
    for _ in range(10):
        # Sélectionne une région non déjà utilisée
        region = random.choice(list(regions.keys()))
        while region in questions_posees:
            region = random.choice(list(regions.keys()))
        
        questions_posees.add(region)
        
        # Pose la question
        print(f"\nQuel est le chef-lieu de la région de : '{region}' ?")
        reponse = input("Votre réponse :  ")
        
        if reponse.lower() == regions[region].lower(): #lower() pour permettre a l'utilisateur de saisir en minuscule ou en majuscule
            print("Bonne réponse !")
            Note += 1
            Score +=50
        else:
            print(f"Réponse Incorrecte!!!")
            print(f"Le chef-lieu de {region} est {regions[region]}")
    print(10*"*")        
    print(f'Pseudo: {Pseudo}')
    print(f'Score: {Score} points')
    print(f"Fin du jeu, Vous avez : {Note} reponses correctes/10")
    print(10*"*")   
    meilleurs_scores.append(Score)

# Menu principal
while True:
    print("\n*** BIENVENUE DANS LE MENU GENERAL DU JEU ***")
    print("1. Jouer ")
    print("2. Quitter")
    choix = input("Votre choix : ")
    
    if choix == "1":
        jouer()
        print("\nVeux-tu effectuer une autre partie ?[o/n]")
        choix_autre = input("Votre reponse  ")
        if choix_autre=="o":
            jouer()
        else:
             print("BYE BYE!!!")
             break   
    elif choix == "2":
        print("BYE BYE!!!")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
