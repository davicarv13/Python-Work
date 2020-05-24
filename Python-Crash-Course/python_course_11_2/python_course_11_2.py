import unittest 

from function import concat_city_country

class TestConcatenation(unittest.TestCase):
	def test_concat_city_country(self):
		result = concat_city_country('santiago', 'chile')
		self.assertEqual(result, "Santiago, Chile")

	def test_city_country_population(self):
		result = concat_city_country('santiago', 'chile', 5000)
		self.assertEqual(result, "Santiago, Chile - Population 5000")		

unittest.main()
