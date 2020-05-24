animal1 = {
	'kind' : 'dog',
	'owner' : 'Davi'
}

animal2 = {
	'kind' : 'cat',
	'owner' : 'Silas'
}

animal3 = {
	'kind' : 'chicken',
	'owner' : 'Zenilda'
}

pets = [animal1, animal2, animal3]

for pet in pets:
	for key, value in pet.items():
		print(str(key) + " : " + str(value))

	print('------------')