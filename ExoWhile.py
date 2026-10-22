# # Liste des éléves
students = ["seb", "quentin", "sandrine", "jerome", "fatima", "gael"]
# # iterration qui va servir à compter
i = 0
# # Fonction while pour la boucle
# # Tant que i< a la longueur de la liste la boucle continue
while i < len(students):
#     # Fonction qui sert a afficher uniquement les noms <= a 5 lettres
    if len(students[i]) <= 5:
        print(students[i])
    i = i + 1

# Exo 2
i = 10
while i > 0:
    print(i)
    i -= 1
print("décollage")

# Exo 3
i = 1
while i <= 3:
    print(i)
    i = i + 1
print("Soleil")

# Exo 4
i = 2
print("Franklin sait compter 2 par 2")
while i <= 10:
    print(i)
    i = i + 2
print("Bravo Franklin !")