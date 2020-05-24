def car_store(manufacturer, model, **informations):
	car_info = {}
	car_info['manufacturer'] = manufacturer
	car_info['model'] = model
	for key, value in informations.items():
		car_info[key] = value
	return car_info


car = car_store('subaru', 'outback', color='blue', tow_package=True)

print(car)