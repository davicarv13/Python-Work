def concat_city_country(city, country, population = ''):
	if population:
		return (city + ", " + country + " - population " + str(population)).title()
	else:
		return (city + ", " + country).title()
