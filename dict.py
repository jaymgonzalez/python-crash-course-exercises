# Debs dictionary 
debs = {
    'name': 'debs',
    'surname': 'deriu',
    'age': 31,
    'city': 'sassari'
}
# print(debs['name'])
# print(debs['surname'])
# print(debs['age'])
# print(debs['city'])

for key,value in debs.items():
    print(f'This person {key} is {value}')

# favourite number
fav_num = {
    'jay': 5,
    'debs': 3,
    'illari': 9,
    'ivan': 6,
    'paolo': 8
}
for key,value in fav_num.items():
    print(f'{key.title()}\'s favourite number is {value}')

# loop through keys
fav_num = {
    'jay': 5,
    'debs': 3,
    'illari': 9,
    'ivan': 6,
    'paolo': 8
}
for key in fav_num.keys():
    print(f'{key.title()}\'s favourite number is undefined')

# loop through unique values
fav_num = {
    'jay': 5,
    'debs': 3,
    'illari': 9,
    'ivan': 8,
    'paolo': 8
}
for value in set(fav_num.values()):
    print(f'the folowing value has been choosen\n{value}')

# Fav num poll
friends = ['jay', 'debs', 'illari', 'ivan', 'paolo', 'marine', 'emanuella', 'giomari']
fav_num = {
    'jay': 5,
    'debs': 3,
    'illari': 9,
    'ivan': 8,
    'paolo': 8
}
for friend in friends:
    if friend in fav_num.keys():
        print(f'Thanks {friend} for participating')
    else:
        print(f'Please {friend} tell me your fav num')

# Dictionary within dictionary
users = {
    'debs': {
        'name': 'debs',
        'surname': 'deriu',
        'age': 31,
        'city': 'sassari'
    },
    'jay': {
        'name': 'jay',
        'surname': 'gonzalez',
        'age': 34,
        'city': 'sassari'
    },
    'gordo': {
        'name': 'jullien',
        'surname': 'lloveras',
        'age': 35,
        'city': 'buenos aires'
    },
}
for user, details in users.items():
    full_name = details['name'] + ' ' + details['surname']
    print(f'{user} full name is: {full_name}')

# Dict of animals
paquito = {
  'type': 'cat',
  'owner': 'jay'
},
eva = {
  'type': 'dog',
  'owner': 'ivan'
},
biaggo = {
  'type': 'cat',
  'owner': 'marine'
},
ettore = {
  'type': 'dog',
  'owner': 'marine'
},
pets = [paquito, eva, biaggo, ettore]

for pet in pets:
    print(pet)

# Fav places
fav_places = {
    'jay': [
        'cali',
        'mazunte',
        'pai'
    ],
    'debs': [
        'brighton',
        'sassari'
    ],
    'paco': [
        'robledo'
    ]
}
for name, places in fav_places.items():
    print(f'{name} favourite places are {places}')

# Cities
cities = {
    'madrid': {
        'population': 4500000,
        'language': 'spanish',
        'country': 'spain'
    },
    'sassari': {
        'population': 150000,
        'language': 'italian',
        'country': 'italy'
    },
    'brighton': {
        'population': 250000,
        'language': 'english',
        'country': 'uk'
    }
}
for name, data in cities.items():
    print(f'{name.title()} has {data["population"]} inhabitants, they speak {data["language"]} 
        and the country it\'s {data["country"]}')