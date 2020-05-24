age = ""

while age != 'quit':
	age = input("Enter your age (Enter 'quit' to exit):	")
	if age == 'quit':
		break
	else:
		age = int(age)
		if age < 3:
			print("Ticket is free")
		elif age >= 3 and age <=12: 
			print("Ticket is $10")
		elif age > 12:
			print("Ticket is $15")
