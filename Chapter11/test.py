import unittest
from formatname import formatted_name
class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        correct_name = formatted_name('janis','joplin')
        self.assertEqual(correct_name, 'Janis Joplin')
    def test_first_middle_last_name(self):
        correct_name = formatted_name('Olabinjo', 'Lagbina', 'Joe')
        self.assertEqual(correct_name, 'Olabinjo Joe Lagbina')
if __name__ == '__main__':
    unittest.main()