import json 

def read_number():
	try:
		with open('favorite_number.json') as file:
			number = json.load(file)
	except FileNotFoundError:
		return None
	except json.decoder.JSONDecodeError:
		return None
	else:
		return number

def store_number(number):
	try:
		with open('favorite_number.json', 'w') as file:
			json.dump(number, file)
	except FileNotFoundError:
		return "File not found"
	else:
		return "Number stored"

def convert_number(number):
	try:
		number = int(number)
	except ValueError:
		return None
	else:
		return number

number = read_number()

if number:
	print('Favorite number is ' + str(number))
else:
	number = input("Type a number:")
	number = convert_number(number)

	while number == None:
		print("You did not entered a number")
		number = input("Type a number:")
		number = convert_number(number)

	print(store_number(number))

	