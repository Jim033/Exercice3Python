mot_secret = "internet"
essais = 6
# Liste vide []
lettres_trouvees = []

while essais > 0:

    lettre = input("Choisis une lettre : ")

    if lettre in mot_secret:
        print("Bonne lettre !")
        # .append() sert à ajouter un élément à la fin d'une liste.
        lettres_trouvees.append(lettre)
    else:
        essais = essais - 1
        print("Mauvaise lettre !")

    print(f"Il te reste {essais} essais.")

    gagne = True
    i = 0
    while i < len(mot_secret):
        # In : Vérifie si quelque chose est présent.
        if mot_secret[i] in lettres_trouvees:
            # est-ce que cette lettre a déjà été trouvée par le joueur ?
            print(mot_secret[i], end=" ")
        else:
            # End : Empêche le retour à la ligne après un print().
            print("_", end=" ")
            gagne = False
        i = i + 1
    print()
    if gagne:
        print(f"Bravo ! Tu as trouvé le mot : {mot_secret}")
        # Break arrête la boucle
        break
if essais == 0:
    print(f"Perdu ! Le mot était : {mot_secret}")