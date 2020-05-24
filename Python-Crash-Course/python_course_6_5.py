rivers = {
	'Nile' : 'Egypt',
	'Paraiba do Sul' : 'Brazil',
	'Solimoes' : 'Brazil',
	'Nile' : 'Egypt'
}

for key, value in set(rivers.items()):
	print(key + " runs through " + value)

print("--------------------")

for key in sorted(set(rivers.keys())):
	print(key)

print("--------------------")

for value in sorted(set(rivers.values())):
	print(value)