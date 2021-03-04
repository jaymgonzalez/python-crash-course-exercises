import unittest
# from city_functions import city_country


# class CityCountryTestCase(unittest.TestCase):
#     '''Test for city country function'''

#     def test_city_country(self):
#         '''Does it return city and country formatted correctly'''

#         city_and_country = city_country('MADRID', 'ESPana')
#         self.assertEqual(city_and_country,
#                          'Madrid, Espana - unknown inhabitants')

#     def test_city_population(self):
#         '''does it run with parameters city, country and population'''

#         city_country_population = city_country('Sassari', 'ItaLia', '150,000')
#         self.assertEqual(city_country_population,
#                          'Sassari, Italia - 150,000 inhabitants')

# unittest.main()

from classes import Employee


class EmployeeTestCase(unittest.TestCase):
    '''Test for the employee class'''

    def setUp(self):
        '''Create set of caracteristics for the employee'''
        self.my_employee = Employee('jay', 'gonzalez', 45000)

    def test_give_default_raise(self):
        '''test that the employee see the salary incremented in 5000'''
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 50000)

    def test_give_custom_raise(self):
        '''test that a custom quantity in give raise f(x) is added correctly to the salary'''
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.salary, 55000)


unittest.main()
