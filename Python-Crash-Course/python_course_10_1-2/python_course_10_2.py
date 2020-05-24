with open('file.txt') as file:
	string = ''
	for line in file:
		string += line

	string.replace('Python', 'C')

	print(string)