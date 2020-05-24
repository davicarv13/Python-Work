class User():
	"""This class represents a common user"""

	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	"""This method prints all user's info"""
	def describe_user(self):
		print(self.first_name + " " + self.last_name + " - " + str(self.age))

	"""This method greets a user"""
	def greet_user(self):
		print("Welcome, " + self.first_name + " " + self.last_name)