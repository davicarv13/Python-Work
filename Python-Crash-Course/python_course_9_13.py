from collections import OrderedDict

programming_words = OrderedDict()

programming_words['HTML'] = 'HyperText Markup Language'
programming_words['OO'] = 'Object Oriented'
programming_words['KISS'] = 'Keep It Simple'
programming_words['Duck_Typing'] = 'Concept for modelling objects that says if'

for key, value in programming_words.items():
	print(key + " : " + value)
