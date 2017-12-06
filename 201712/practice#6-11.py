cities = {
    'canton': {
        'country': 'china',
        'population': '1404w',
        'fact': 'eat eat eat',
        },

    'los angles': {
        'country': 'america',
        'population': '397w',
        'fact' : 'lakers',
        },

    'paris': {
        'country': 'franch',
        'population': '242w',
        'fact': 'the eiffel tower',
        },
    }

for city,info in cities.items():
    print("\n" + city.title() + "'s information")
    for key,value in info.items():
        print("\t" + key.title() + ": " + value)