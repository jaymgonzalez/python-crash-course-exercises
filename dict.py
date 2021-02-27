# # Debs dictionary 
# debs = {
#     'name': 'debs',
#     'surname': 'deriu',
#     'age': 31,
#     'city': 'sassari'
# }
# # print(debs['name'])
# # print(debs['surname'])
# # print(debs['age'])
# # print(debs['city'])

# for key,value in debs.items():
#     print(f'This person {key} is {value}')

# # favourite number
# fav_num = {
#     'jay': 5,
#     'debs': 3,
#     'illari': 9,
#     'ivan': 6,
#     'paolo': 8
# }
# for key,value in fav_num.items():
#     print(f'{key.title()}\'s favourite number is {value}')

# # loop through keys
# fav_num = {
#     'jay': 5,
#     'debs': 3,
#     'illari': 9,
#     'ivan': 6,
#     'paolo': 8
# }
# for key in fav_num.keys():
#     print(f'{key.title()}\'s favourite number is undefined')

# # loop through unique values
# fav_num = {
#     'jay': 5,
#     'debs': 3,
#     'illari': 9,
#     'ivan': 8,
#     'paolo': 8
# }
# for value in set(fav_num.values()):
#     print(f'the folowing value has been choosen\n{value}')

# # Fav num poll
# friends = ['jay', 'debs', 'illari', 'ivan', 'paolo', 'marine', 'emanuella', 'giomari']
# fav_num = {
#     'jay': 5,
#     'debs': 3,
#     'illari': 9,
#     'ivan': 8,
#     'paolo': 8
# }
# for friend in friends:
#     if friend in fav_num.keys():
#         print(f'Thanks {friend} for participating')
#     else:
#         print(f'Please {friend} tell me your fav num')

