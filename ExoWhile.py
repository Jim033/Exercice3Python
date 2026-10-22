# Afficher les nombres de 1 à 10
i = 1
while i <= 10:
    print(i)
    i = i + 1

# Afficher les nombre de 10 à 1
i = 10
while i > 0:
    print(i)
    i -= 1
# Afficher les nombre pairs de 20 a 2
i = 20
while i >= 2:
    print(i)
    i -= 2
# Calculer la somme de ces nombres 423 5435 654 234 765
number = [423, 5435, 654, 234, 765]
i = 0
total = 0
while i < len(number):
    total = total + number[i]
    i = i + 1
print(f"La somme est : {total}")
# Calculer la moyenne des notes de cette classe 14 16 1 17 8
notes = [14, 16, 1, 17, 8]
i = 0
total = 0
while i < len(notes):
    total = total + notes[i]
    i = i + 1
moyenne = total / len(notes)

print(f"La moyenne est : {moyenne}")

# Calculer la somme des nombres de 1 a 100
i = 0
total = 0
while i <= 100:
    total = total + i
    i = i + 1
print(total)

# Poser la question "vas tu réussir dans le dev ?" dans la console et la reposer en boucle tant que la réponse n'est pas oui

reponse = ""
while reponse != "oui":
    reponse = input("Vas-tu réussir dans le dev ? ")
    if reponse == "oui":
        print("Je le savais !")
    else:
        print("Essaie encore !")