# Restaurant
class Restaurant():
    '''A simple class for a restaurant'''

    def __init__(self, name, cousin_type):
        self.name = name
        self.cousin_type = cousin_type
        self.number_served = 0

    def describe_restaurant(self):
        '''Method to describe the restaurant'''

        print(
            f'This restaurant it\'s called {self.name} and the type of food is {self.cousin_type}')

    def open_restaurant(self):
        '''Method to describe the restaurant'''

        print('Come and visit us, the restaurant is open!')

    def set_number_served(self, number):
        '''set how many people have been served'''

        self.number_served = number

    def increment_number_served(self, number):
        '''increment the number of tables served'''

        self.number_served += number


# restaurant = Restaurant('Yakitoro', 'Asian mix')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# restaurant2 = Restaurant('tula', 'spanish')
# restaurant3 = Restaurant('tritus', 'italian')
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()

# User
class User():
    '''Class to define users'''

    def __init__(self, first_name, last_name, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.login_attempts = 0

    def describe_user(self):
        '''Describe user properties in a sentence'''

        print(
            f'User full name is {self.first_name.title()} {self.last_name.title()}, his telephone is {self.phone} and his email address is {self.email}')

    def greet_user(self):
        '''Greet the user with personalize message'''

        print(f'Hey {self.first_name.title()}, welcome back!')

    def increment_login_attempts(self):
        '''increment every time user have tried to log in'''

        self.login_attempts += 1

    def reset_login_attempts(self):
        '''set log in attempts back to 0'''

        self.login_attempts = 0


# user = User('jay', 'gonzalez', 'juju@gmail.com', '69696969696')
# user2 = User('debs', 'deriu', 'jojo@gmail.com', '5454545454')
# user.describe_user()
# user2.describe_user()
# user.greet_user()
# user2.greet_user()

# # Restaurant 2
# restaurant = Restaurant('maccy d', 'fast food')
# print(restaurant.number_served)
# restaurant.number_served = 3456
# print(restaurant.number_served)
# restaurant.set_number_served(10)
# print(restaurant.number_served)
# restaurant.increment_number_served(150)
# print(restaurant.number_served)

# # Login attempts
# user = User('jay', 'gonzalez', 'juju@gmail.com', '69696969696')
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# print(user.login_attempts)
# user.reset_login_attempts()
# print(user.login_attempts)

# Ice cream stand
class IceCreamStand(Restaurant):
    '''class for ice cream stand restaurant'''

    def __init__(self, name, cousin_type):
        super().__init__(name, cousin_type)
        self.flavours = ['nocciola', 'pistacchio', 'chocolatto']

    def display_flavours(self):
        '''display flavours available'''

        print('We have the following flavours available:')
        for flavour in self.flavours:
            print(f'- {flavour}')


# ice_cream = IceCreamStand('b&j', 'ice cream stand')
# ice_cream.display_flavours()

# Privileges class

class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can ban user', 'can delete post']

    def show_privileges(self):
        '''print privileges that admin user has'''

        print(f'The user has the following admin privileges:')
        for privilege in self.privileges:
            print(f'- {privilege}')

# Admin


class Admin(User):
    '''admin user subclass within user class'''

    def __init__(self, first_name, last_name, email, phone):
        super().__init__(first_name, last_name, email, phone)
        self.privileges = Privileges()

# admin = Admin('jay', 'gonzalez', 'juju@gmail.com', '69696969696')
# admin.privileges.show_privileges()
