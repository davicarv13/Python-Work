cities = {
	'Campos dos Goytacazes': {
		'Country' : 'Brazil', 
		'Population' : 250000,
		'Fact' : "Land of 'Chuvisco'"
	},
	'Macae': {
		'Country' : 'Brazil', 
		'Population' : 15000,
		'Fact' : "Land of black gold"	
	},
	'Quissama': {
		'Country' : 'Brazil', 
		'Population' : 50000,
		'Fact' : "Small city"
	},
}

for city, facts in cities.items():
	print(city + "'s facts: ")
	for key, value in facts.items():
		print(key + " : " + str(value))

	print("-----------")