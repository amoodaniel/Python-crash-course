import unittest
from City_function import city_country
class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        correct_value = city_country('lagos', 'nigeria')
        self.assertEqual(correct_value, 'Lagos, Nigeria')
    def test_city_country_population(self):
        correct_value = city_country('lagos','nigeria', '120000000')
        self.assertEqual(correct_value, 'Lagos, Nigeria Population = 120000000')

if __name__ == '__main__':
    unittest.main()
