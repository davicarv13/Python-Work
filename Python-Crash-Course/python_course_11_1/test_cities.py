import unittest

from function import concat_city_country

class test_cities(unittest.TestCase):
	def test_city_country(self):
		"""Test city-country concatenation"""
		formatted_city_country = concat_city_country('santiago', 'chile')
		self.assertEqual(formatted_city_country, 'Santiago, Chile')

unittest.main()

