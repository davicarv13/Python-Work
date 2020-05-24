sandwich_orders = ['Calabresa', 'Pastrami', 'Presunto', 'Pastrami', 'Queijo', 'Carne', 'Pastrami']

finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	if sandwich.lower() != 'pastrami':
		print("I made your " + sandwich)
		finished_sandwiches.append(sandwich)

print("Finished sandwiches. Sadly Deli ran out of Pastrami.")
for sandwich in finished_sandwiches:
	print(sandwich)
