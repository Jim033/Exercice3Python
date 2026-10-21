fruits = ["banane", "mangue"]
newfruit = input("Quel fruit veux tu ajouter ? ")
fruits.append(newfruit)
len_fruits = len(fruits)
print(f"Notre nouveau tableau de fruits est {fruits}")
print(f"Nous avons {len_fruits} fruits dans notre panier")