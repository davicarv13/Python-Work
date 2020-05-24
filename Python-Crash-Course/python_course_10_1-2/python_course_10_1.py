with open('file.txt') as file:
	print("---Reading line by line:---\n")
	for line in file:
		print(line.rstrip())

	print('-----------')


with open('file.txt') as file:
	print("---Reading entire file:---\n")
	contents = file.read()
	print(contents.rstrip())

	print('-----------')

with open('file.txt') as file:
	lines = file.readlines()

string = ''

print('--Working with files---\n')
for line in lines:
	string += '- ' + line 

print(string)

