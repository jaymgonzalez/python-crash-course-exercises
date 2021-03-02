# Display message
def display_message():
    print('I\'m learning about functions')
display_message()

# Display Book
def favourite_book(book):
    print(f'One of my favourite books is {book}')
favourite_book('santaran')

# T-shirt
def make_tshirt(size, message):
    print(f'The selected T-shirt it\'s size {size} and the message is: {message}')

make_tshirt('M', 'I\'m the best')
make_tshirt(message='Hollow world!', size='XL')

# New T-shirt
def make_tshirt(size='L', message='I <3 Python'):
    print(f'The selected T-shirt it\'s size {size} and the message is: {message}')

make_tshirt()
make_tshirt('M')

# Cities and countries
def describe_city(city, country='italy'):
    print(f'{city} is in {country}')

describe_city('rome')
describe_city('madrid', 'spain')

# Cities and countries 2
def city_country(city, country='italy'):
    print(f'{city.title()}, {country.title()}')

city_country('madrid', 'spain')
city_country('rome', 'italy')

# Album
def make_album(artist, title, num_of_tracks=''):
    if num_of_tracks:
        return {
            'artist': artist,
            'album title': title,
            'number of tracks': num_of_tracks,
        }
    else:
        return {
            'artist': artist,
            'album title': title,
       }

beattles = make_album('the beattles', 'yellow submarine')
ozuna = make_album('ozuna', 'las paga todas', 12)

print(beattles, ozuna)

# User album
def make_album(artist, title, num_of_tracks=''):
    if num_of_tracks:
        return {
            'artist': artist,
            'album title': title,
            'number of tracks': num_of_tracks,
        }
    else:
        return {
            'artist': artist,
            'album title': title,
       }

while True:
    album = input('Please enter album name. ')
    artist = input('Please enter artist name. ')
    if album == 'q' or artist == 'q':
        print('Exiting the program...')
        break
    else:
        new_entry = make_album(artist, album)
        print(new_entry)

# Magicians
magicians = ['juan tamariz', 'el otro', 'el de la moto', 'david coperfield']
def show_magicians(list):
    for magician in list:
        print(f'El nombre del mago es {magician}')

show_magicians(magicians)

# Magicians 2
magicians = ['juan tamariz', 'el otro', 'el de la moto', 'david coperfield']
great_magicians = []

def show_magicians(list):
    for magician in list:
        print(f'El nombre del mago es {magician}')

def make_great(list, updated_list):
    while list:
        magician = list.pop()
        magician += ' The great'
        updated_list.append(magician)

make_great(magicians[:], great_magicians)
show_magicians(great_magicians)
show_magicians(magicians)

# Sandwiches
def sandwich(*toppings):
    print('The sandwich you ordered has the following ingridients:')
    for topping in toppings:
        print(f'- {topping}')

sandwich('tomatoes', 'bacon', 'avocado', 'mayo')
sandwich('lettice', 'onion', 'egg')
sandwich('burger', 'cheese', 'bbq sauce')

# User profile
def user_profile(first, last, **user_info):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for title, data in user_info.items():
        profile[title] = data

    return profile

jay = user_profile('jaime', 'gonzalez', born_in='madrid', supporter='Real Madrid', ocuppation='programmer')
print(jay)
