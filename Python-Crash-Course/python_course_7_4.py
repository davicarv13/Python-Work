pizza_toppings = []

topping = ""


while topping != 'quit':
	topping = input("Enter a topping (Enter 'quit' for exit): ")
	if(topping == 'quit'):
		break
	else:
		print("Adding " + topping + " to the pizza")
		pizza_toppings.append(topping)