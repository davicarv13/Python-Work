import json

def read_number():
	try:
		with open('favorite_number.json', 'r') as file:
			number = json.load(file)
	except FileNotFoundError:
		return "error"
	else:
		return number

number = read_number()

if number == 'error':
	print('File not found')
else:
	print("I know your favorite number. It's " + str(number))
