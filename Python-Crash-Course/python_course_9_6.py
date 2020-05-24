class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(self.restaurant_name + " - " + self.cuisine_type)

	def open_restaurant(self):
		print("The restaurant is open")

class IceCreamStan(Restaurant):
	def __init__(self, restaurant_name, cuisine_type, *flavors):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors

	def display_flavors(self):
		all_flavors = ""
		for flavor in self.flavors:
			all_flavors += flavor + ", "
		return all_flavors


iceCreamRest = IceCreamStan('Joanne Trattoria', 'Italian', 'Strawberry', 'Chocolate', 'Peach')


print(iceCreamRest.display_flavors())

