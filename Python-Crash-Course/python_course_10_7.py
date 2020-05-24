def string_convert(number):
	try:
		number = int(number)
	except ValueError:
		return "error"
	else:
		return number


number1 = input("Enter a number:")

number1 = string_convert(number1)

while number1 == "error":
	print("You did not entered a number:")
	number1 = input("Enter a number")	
	number1 = string_convert(number1)

number2 = input("Enter a nother number:")

number2 = string_convert(number2)

while number2 == "error":
	print("You did not entered a number:")
	number2 = input("Enter a number:")	
	number2 = string_convert(number2)

sum = number1 + number2

print(str(number1) + " + " + str(number2) + " = " + str(sum))

