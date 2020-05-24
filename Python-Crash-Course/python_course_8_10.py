def make_great(magicians_list):
	index = 0
	while index < len(magicians_list):
		magicians_list[index] = "Great " + magicians_list[index]
		index = index + 1

def print_magicians(magicians_list):
	for magician in magicians_names:
		print(magician)

magicians_names = ['Merlin', 'Bonny', 'Medusa']

make_great(magicians_names)
print_magicians(magicians_names)