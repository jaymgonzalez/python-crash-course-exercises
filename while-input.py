# # Rent a car
# car = input('What kind of car would you like to rent? ')
# print(f'Let me see if we have a {car}')

# # Restaurant
# attendees = input('How many people are in the dinner group? ')

# if int(attendees) >= 8:
#     print('Please wait until I set your table up')
# else:
#     print('Please follow me')

# # Multiple of 10
# number = input('Enter a number and I\'ll tell you if it\'s multiple of 10. ')
# if int(number) % 10 == 0:
#     print(f'{number} it\'s multiple of 10')
# else:
#     print(f'{number} is not multiple of 10')

# # Pizza topping
# while True:
#     message = 'Please enter your pizza topping'
#     message += '\nTo end write quit. '
#     ingredient = input(message)
#     if ingredient != 'quit':
#         print(f'Adding {ingredient} to your pizza')
#     else:
#         break

# # Movie theather
# age = int(input('How old are you? '))
# if age <= 3:
#     print('Your ticket is free')
# elif age <= 12:
#     print('Your ticket is 10$')
# else:
#     print('Your ticket is 15$')

# # Pizza topping with flag
# active = True
# while active:
#     message = 'Please enter your pizza topping'
#     message += '\nTo end write quit. '
#     ingredient = input(message)
#     if ingredient != 'quit':
#         print(f'Adding {ingredient} to your pizza')
#     else:
#         active = False

# # Sandwich Deli
# sandwich_orders = ['blt', 'avocado salad', 'pastrami', 'salami', 'pastrami', 'blt', 'bacon']
# finished_sandwich = []

# while sandwich_orders:
#     current = sandwich_orders.pop()
#     finished_sandwich.append(current)
#     print(f'{current} sandwich done')

# # No pastrami
# sandwich_orders = ['blt', 'avocado salad', 'pastrami', 'salami', 'pastrami', 'blt', 'bacon']

# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# print(sandwich_orders)

# # Vacation destination
# dreamed_vacations = {}
# active = True

# while active:
#     name = input('What is your name? ')
#     vacation = input('What would be your favourite place to go? ')

#     dreamed_vacations[name] = vacation
#     flag = input('Does anyone else wants to response? ')
#     if flag == 'no':
#         active = False

# for name, destination in dreamed_vacations.items():
#     print(f'{name} favourite destination is {destination}')