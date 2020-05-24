person1 = {
	'first_name': 'Davi', 
	'last_name' : 'Carvalho', 
	'age' : 22,
	'city' : 'Campos dos Goytacazes'
	}

person2 = {
	'first_name': 'Silas', 
	'last_name' : 'Carvalho', 
	'age' : 21,
	'city' : 'Campos dos Goytacazes'
}

person3 = {
	'first_name': 'Debora', 
	'last_name' : 'Carvalho', 
	'age' : 29,
	'city' : 'Campos dos Goytacazes'
}

people = [person1, person2, person3]

for person in people:
	for key, value in person.items():
		print(str(key) + " : " + str(value))

	print('----------------')
 