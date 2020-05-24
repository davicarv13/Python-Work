favorite_numbers = {
	'Davi' : [13, 31],
	'Silas' : [2, 6, 1],
	'Moma' : [7, 8, 4]
}

for person, number_list in favorite_numbers.items():
	print(person + " favorite's numbers are: ")
	for number in number_list:
		print(number);
