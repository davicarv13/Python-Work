def record_visit(name):
	with open('guest_book.txt', 'a') as file:
		file.write(name + ' visited us.\n')

name = ''
print("Print 'q' to quit:")

while name != 'q':
	name = input('Enter your name:')
	if name != 'q':
		print("Hello, " + name)
		record_visit(name)	
	else:
		print('Bye')
	
	