from user import User

class Privileges():
	"""This class reprents privileges of a admin user"""

	def __init__(self, *privileges):
		self.privileges = privileges

	def show_privileges(self):
		message = "Privileges: \n"

		for privilege in self.privileges:
			if privilege == self.privileges[-1]:
				message += privilege
			else:
				message += privilege + ", "

		return message

class Admin(User):
	"""This class represents an administrator of the system"""
	
	def __init__(self, first_name, last_name, age, privileges):
		super().__init__(first_name, last_name, age)
		self.privileges = privileges
