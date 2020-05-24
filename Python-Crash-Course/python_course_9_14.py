from random import randint

"""Generates random numbers"""

class Die():
	"""This class represents a die and it's methods"""
	
	def __init__(self, sides = 6):
		self.sides = sides

	def roll_die(self):
		return randint(1, self.sides)

six_sided_die = Die()
ten_sided_die = Die(10)
twenty_sided_die = Die(20)

print("Rolling 6-sided die:")
for cont in range(1, 10):
	print(six_sided_die.roll_die())

print("Rolling 10-sided die:")
for cont in range(1, 10):
	print(ten_sided_die.roll_die())

print("Rolling 20-sided die:")
for cont in range(1, 20):
	print(twenty_sided_die.roll_die())