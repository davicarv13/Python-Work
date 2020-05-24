class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(self.restaurant_name + " - " + self.cuisine_type)

	def open_restaurant(self):
		print("The restaurant is open")

restaurant1 = Restaurant("Joanne Trattoria", "Italian")
restaurant2 = Restaurant("Michellin", "European")
restaurant3 = Restaurant("Joanne Trattoria", "Italian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()