def read_file(filename):
	try:

		with open(filename) as file:
			contents = file.read()
	except FileNotFoundError:
		return "File not found"
	else:
		message = ''
		for line in contents:
			message += line
		return message

print(read_file('cats.txt'))
print(read_file('dogs.txt'))
