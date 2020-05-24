favorite_places = {
	'Davi': ['Paris', 'France', 'Japan'],
	'Silas': ['USA', 'Canada', 'Italy'],
	'Zenilda': ['Brazil', 'China', "Chile"]
}

for person, place_list in sorted(favorite_places.items()):
	print(person + " favorite's places: ")
	for place in place_list:
		print(place)
	print("-----------")