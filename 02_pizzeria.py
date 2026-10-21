nombre_pizzas = int(input("Combien de pizzas ?"))
prix_pizza = float(input("Prix d'une pizza ?"))

total = nombre_pizzas * prix_pizza

reduction = 0

if nombre_pizzas > 5:
    reduction = total * 0.10

total = total - reduction

livraison = 0

if total < 20:
    livraison = 3

total = total + livraison

print("=== PIZZA TICKET ===")
print(f"Pizzas : {nombre_pizzas} x {prix_pizza} euros")
print(f"Réduction : -{reduction} euros")

if livraison == 0:
    print("Livraison : gratuite")
else:
    print(f"Livraison : {livraison} euros")

print(f"Total : {total} euros")