# # counting to 20
# count = list(range(1,21))
# for value in count:
#     print(value)

# # counting to one million
# count_1_million = list(range(1,1000000))
# for value in count_1_million:
#     print(value)

# # find min max and the sum of 1 to a million
# count_1_million = list(range(1,1000000))
# result_list = []
# for value in count_1_million:
#     result_list.append(value)
# print(min(result_list))
# print(max(result_list))
# print(sum(result_list))

# # Odd numbers
# odd_numbers = list(range(1, 20, 2))
# for value in odd_numbers:
#     print(value)

# # Thress
# multiples_of_three = list(range(3, 30, 3))
# for value in multiples_of_three:
#     print(value)

# # Cubes
# first_10_cubes = []
# numbers = list(range(1,11))
# for value in numbers:
#     first_10_cubes.append(value**3)
# print(first_10_cubes)

# # Cubes list comprehension
# cubes = [value**3 for value in range(1, 11)]
# print(cubes)

# # Slices - First 3 items
# cubes = [value**3 for value in range(1, 11)]
# print(f'The fist 3 item in the list are {cubes[:3]}')

# # Slices - 3 items in the middle
# cubes = [value**3 for value in range(1, 11)]
# middle_point = len(cubes)/2
# first = int(middle_point - 1)
# last = int(middle_point + 2)
# print(f'The middle 3 item in the lite are {cubes[first:last]}')

# # Slices - Last 3 items
# cubes = [value**3 for value in range(1, 11)]
# print(f'The fist 3 item in the list are {cubes[-3:]}')

# Copy Lists
# debs_pizza = ['salchichon', 'champinon', 'patata asada', 'pimiento']
# my_pizza = debs_pizza[:]

# my_pizza.append('rucula')
# debs_pizza.append('tomate')

# print(my_pizza)
# print(debs_pizza)

# # Food Tuple
# food = ('pizza', 'pasta', 'albondigas', 'paella', 'ensalada')
# for item in food:
#     print(item)
# # food[0] = 'panino'
# new_food = ('pizza', 'pasta', 'panino', 'paella', 'croquetas')
# for item in food:
#     print(item)
