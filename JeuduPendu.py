mot_secret = "python"
essais = 6
lettres_trouvees = []

while essais > 0:

    lettre = input("Choisis une lettre : ")

    if lettre in mot_secret:
        print("Bonne lettre !")
        lettres_trouvees.append(lettre)
    else:
        essais = essais - 1
        print("Mauvaise lettre !")

    print(f"Il te reste {essais} essais.")

    gagne = True
    i = 0
    while i < len(mot_secret):
        if mot_secret[i] in lettres_trouvees:
            print(mot_secret[i], end=" ")
        else:
            print("_", end=" ")
            gagne = False
        i = i + 1
    print()
    if gagne:
        print(f"Bravo ! Tu as trouvé le mot : {mot_secret}")
        break
if essais == 0:
    print(f"Perdu ! Le mot était : {mot_secret}")