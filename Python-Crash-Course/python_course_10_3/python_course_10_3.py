def write_name(name):
	with open('guest.txt', 'w') as file:
		file.write(name)	

name = input("Enter your name:")
write_name(name)



