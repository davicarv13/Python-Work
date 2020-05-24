class User():
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def describe_user(self):
		print(self.first_name + " " + self.last_name + " - " + str(self.age))

	def greet_user(self):
		print("Welcome, " + self.first_name + " " + self.last_name)


class Privileges():

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
	def __init__(self, first_name, last_name, age, privileges):
		super().__init__(first_name, last_name, age)
		self.privileges = privileges
		
privileges = Privileges('can add post', 'can delete a post')

admin = Admin('Davi', 'Carvalho', 23, privileges)
print(admin.privileges.show_privileges())

