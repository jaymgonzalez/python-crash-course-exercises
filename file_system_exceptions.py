# # read from file
# filename = 'pi.txt'

# # # with info outside the block
# # with open(filename) as file_object:
# #     lines = file_object.readlines()

# # for line in lines:
# #     print(line.rstrip() * 3)

# # with infor within the block
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip() * 3)

# # Writting to empty file
# filename = 'programming.txt'

# # with open(filename, 'w') as file_object:
# #     file_object.write('programming is coooool!\n')
# #     int(file_object.write('2345678\n'))

# # Wrtting to an existing file
# with open(filename, 'a') as file_object:
#     file_object.write('I love creating apps that run in the browser!\n')
#     file_object.write('And make sense of large data sets\n')

# # Program that writes a log of the user
# filename = 'guest.txt'

# name = input('Please enter your name: ')

# with open(filename, 'w') as file_object:
#     file_object.write(name)

# # Guest Book
# filename = 'guest_book.txt'

# print('input "q" to exit at any time')
# while True:
#     name = input('Please enter your name. ')
#     if name == 'q':
#         break
#     print(f'Welcome {name}, you\'ll be added to our guest book')
#     with open(filename, 'a') as file_object:
#         file_object.write(f'{name}\n')

# # programming reasons
# filename = 'reasons.txt'

# print('input "q" to exit at any time')
# while True:
#     reason = input('Please enter the reason you like programming. ')
#     if reason == 'q':
#         break
#     with open(filename, 'a') as file_object:
#         file_object.write(f'{reason}\n')

# # Handling exceptions
# # ZeroDivisionError
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print('You cannot divide by zero!')

# # FileNotFoundError
# filename = 'sir_edwin.txt'


# def count_words(filename):
#     '''Count the number of words in a file'''
#     try:
#         with open(filename) as file_object:
#             content = file_object.read()
#     except FileNotFoundError:
#         # print(f'The file {filename} couldn\'t been found.')
#         # fail silently
#         pass
#     else:
#         words = content.split()
#         num_words = len(words)
#         print(f'The file {filename} has approximately {num_words} words.')


# filenames = ['sir_edwin.txt', 'siddartha.txt', 'letters.txt', 'studies.txt']

# for book in filenames:
#     count_words(book)

# TypeError exception
num_1 = input('Please enter first number to add. ')
num_2 = input('Please enter second number to add. ')

try:
    int(num_1)
    int(num_2)
except ValueError:
    print('Please provide a valid number')
else:
    addition = int(num_1) + int(num_2)
    print(addition)
