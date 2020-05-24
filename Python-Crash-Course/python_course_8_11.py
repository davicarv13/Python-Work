def make_great(magicians_list, *arguments):
	index = 0
	while index < len(magicians_list):
		magicians_list[index] = "Great " + magicians_list[index]
		index = index + 1

	return magicians_list

def print_magicians(magicians_list):
	for magician in magicians_list:
		print(magician)

magicians_list = ['Merlin', 'Bonny', 'Medusa']

modified_list = make_great(magicians_list[:])

print_magicians(magicians_list)
print_magicians(modified_list)