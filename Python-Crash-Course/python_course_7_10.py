favorite_places = []

answer = ""

while answer != 'quit':
	answer = input("If you could visit one place in the world, where would you go?")
	if answer != 'quit':
		favorite_places.append(answer)

print("Results of the poll:")
for place in favorite_places:
	print(place)

