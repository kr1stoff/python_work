favorite_places = {
    'kristoff':['paris','los angles','istanbul'],
    'silin':['kyoto','osaka','hokkaido'],
    'jiuw':['london','madrid'],
    }

for name,places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place)