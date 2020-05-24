import json 

def store_number(number):
	try:
		with open('favorite_number.json', 'w') as file:
			json.dump(number, file)
	except FileNotFoundError:
		return "File not found"
	else:
		return "Number stored"

def catch_number():
	number = input("Type a number:")

	try:
		number = int(number)
	except ValueError:
		print("You did not entered a number:")
		catch_number()
	else:
		return number

number = catch_number()
print(store_number(number))
