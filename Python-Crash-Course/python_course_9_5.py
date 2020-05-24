class User():
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.login_attempts = 0

	def describe_user(self):
		print(self.first_name + " " + self.last_name + " - " + str(self.age))

	def greet_user(self):
		print("Welcome, " + self.first_name + " " + self.last_name)

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0




user = User('Davi', 'Carvalho', age = 23)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)


