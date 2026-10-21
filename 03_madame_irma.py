name = input("Ton prénom ?")
age = int(input ("Ton age ?"))
birthyear = 2026 - age
Age_10 = age + 10

print(f"Madame Irma voit tout, {name} !")
print(f"Tu es né(e) vers {birthyear}.")
print(f"Dans 10 ans, tu auras {Age_10} ans.")

if age < 18:
    print("Prédiction : Tu aura un 3 au prochain contrôle de philo de demain")
elif age >= 18 and age <=30:
    print("Prédiction : Tu auras un appel d'audi qui t'offre le dernier RS6 ")
elif age >30 and age <=60:
    print("Prédiction : Tu auras un château avec un garage par marque de voiture")
else:
    print("Prédiction : Tu va avoir mal au dos tout les révéils")