score = 0
vie = 3
# Choix 1
print("Tu arrives devant une porte mystérieuse.")
print("1) Frapper")
print("2) Partir")
print("3) Ouvrir la porte")

# Scène 1
choix = int(input("Ton choix ?"))
if choix == 1:
    print("Un gobelin ouvre. Il est très poli ! +10 points")
    score +=10
elif choix == 2:
    print("Tu préfère éviter les ennuis. +5 points")
    score +=5
elif choix == 3:
    print("La porte casse mais un piège se déclenche ! -1 vie")
    vie -= 1

# Choix 2
print("Tu arrives devant un squelette.")
print("1) Tu l'attaque a main nu.")
print("2) Tu t'enfuis.")
print("3) Tu cris à l'aide.")

# Scène 2
choix = int(input("Ton choix ?"))
if choix == 1:
    print("Tu essaye de le battre mais il te frappe avant... -1 vie")
    vie -=1
elif choix == 2:
    print("Tu réussi à t'enfuire bravo ! +10 points")
    score +=10
elif choix == 3:
    print("Tu cris mais personne ne viens et le squelette viens t'attaquer... -1 vie")
    vie -=1

# Choix 3
print("Tu arrives devant 3 coffres du donjon.")
print("1) Tu ouvre le coffre en or.")
print("2) Tu ouvre le coffre en argent.")
print("3) Tu pars sans ouvrir de coffre.")

# Scène 3
choix = int(input("Ton choix ?"))
if choix == 1:
    print("Magnifique des lingots d'or !!! +50 points")
    score +=50
elif choix == 2:
    print("Le coffre étais piéger et une explosion s'active... -1 vie")
    vie -=1
elif choix == 2:
    print("Tu repars en héros mais sans argent ! +5 points")
    score +=5

print(f"Score : {score}")
print(f"Vie : {vie}")
if vie <= 0:
    print("GAME OVER")

if score >= 35:
    print("Légende du donjon")
elif score >= 20:
    print("Aventurier moyen")
else:
    print("Il faut s'entraîner")