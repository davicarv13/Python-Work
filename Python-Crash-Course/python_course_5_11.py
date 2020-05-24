numbers = list(range(1, 10))

for number in numbers:
	if number in range(1, 4):
		print(str(number) + "rd")
	else:
		print(str(number) + "th")
