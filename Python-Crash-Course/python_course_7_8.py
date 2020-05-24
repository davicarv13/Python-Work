sandwich_orders = ['Calabresa', 'Presunto', 'Queijo', 'Carne']

finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print("I made your " + sandwich)
	finished_sandwiches.append(sandwich)

print("Finished sandwiches")
for sandwich in finished_sandwiches:
	print(sandwich)
