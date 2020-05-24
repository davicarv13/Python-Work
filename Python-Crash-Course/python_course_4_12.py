pizzas = ["Cheese", "Meat", "Bacon"]

friend_pizzas = pizzas[:]

pizzas.append("Pepperonis")

print("My pizzas:")
for pizza in pizzas:
	print(pizza)

print("My friend's pizzas:")
for pizza in friend_pizzas:
	print(pizza)	
