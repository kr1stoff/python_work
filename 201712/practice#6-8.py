superman = {
    'type': 'dog',
    'owner': 'kristoff',
    } 

batman = {
    'type': 'bat',
    'owner': 'silin',
    }

wonder_women = {
    'type': 'pig',
    'owner': 'jiuw',
    }

pets = [superman,batman,wonder_women]

for pet in pets:
    for key,value in pet.items():
        print(key.title() + ": " + value)