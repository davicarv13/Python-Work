favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

people = ['maycon', 'jose', 'vinicius', 'jen', 'phil']

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + 
	language.title() + ".")

for person in set(people): 
	if person in favorite_languages : 
		print("Dear " + person + ", thank you for responding.")
	else:
		print("Dear " + person + ", would you like to respond my research?")