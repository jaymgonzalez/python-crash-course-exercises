# # test conditional value
# car = 'Honda'
# print('is car == honda? False')
# print(car == 'honda')
# print('is car == nissan? False')
# print(car == 'nissan')
# print('is car == Honda? True')
# print('Honda' == car.title())

# # Item in list or not
# list_1 = ['pepe', 'paquito', 'fer', 'dani']
# print('paco' in list_1)
# print('paquito' in list_1)
# if 'maria' not in list_1:
#     print('Maria is not in the list')

# # Alien Color 1
# alien_color = 'green'
# if alien_color == 'yellow':
#     print('Player just earned 5 points!')
# else:
#     print('Player just earned 10 points!')
    
# # Alien Color 2
# alien_color = 'yellow'
# if alien_color == 'green':
#     print('Player just earned 5 points!')
# if alien_color == 'yellow':
#     print('Player just earned 10 points!')
# if alien_color == 'red':
#     print('Player just earned 15 points!')

# # Stages of life
# age=14
# if age < 2:
#     print('You are just a baby')
# elif age < 4:
#     print('You are a toddler')
# elif age < 13:
#     print('You are a kid')
# elif age < 20:
#     print('You are a teenager')
# elif age < 60:
#     print('You seem an adult')
# else:
#     print('You are elder')

# # Favourite fruits
# fav_fruits = ['banana', 'papaya', 'mango']
# if 'banana' in fav_fruits:
#     print('I love babanas too')
# if 'mango' in fav_fruits:
#     print('I love mangoes too')
# if 'papaya' in fav_fruits:
#     print('I love papayas too')
# if 'pitaya' not in fav_fruits:
#     print('Ma come e possibile?')
# if 'manzana' not in fav_fruits:
#     print('No te entiendo')

# # Hello admin
# users = ['debs', 'jay', 'marine', 'ivan', 'illari', 'admin']
# # users = []
# if users:   
#     for user in users:
#         if user == 'admin':
#             print(f'Hello {user}, do you want to see a status report?')
#         else:
#             print(f'Hello, {user}, thanks for logging in again')
# else:
#     print('We should add some users')

# #  Checking usernames
# user_names = ['debs', 'jay', 'marine', 'ivan', 'illari', 'admin']
# new_users= ['debs', 'Jay', 'marine', 'pepe', 'paquito']
# for new_user in new_users:
#     if new_user.lower() in user_names:
#         print(f'Sorry, {new_user} is already in use, choose another user name')
#     else:
#         print(f'Welcome {new_user}!')

# # Ordinal numbers
# numbers = list(range(1,10))
# for number in numbers:
#     if number == 1:
#         print(f'{number}st')
#     elif number == 2:
#         print(f'{number}nd')
#     elif number == 3:
#         print(f'{number}rd')
#     else:
#         print(f'{number}th')
