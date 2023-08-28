import unittest
from Employee import Employee

class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.new_employee = Employee('Dapo', 'Turbana', 12000)
    
    def test_default_raise(self):
        self.new_employee.give_raise()
        self.assertEqual(self.new_employee.salary,17000)
    
    def test_custom_raise(self):
        self.new_employee.give_raise(10000)
        self.assertEqual(self.new_employee.salary,22000)
    
if __name__ == '__main__':
    unittest.main()
