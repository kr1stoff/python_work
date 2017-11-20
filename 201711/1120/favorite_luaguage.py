favorite_luaguage = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name,luaguages in favorite_luaguage.items():
    if len(luaguages) == 1:
        for luaguage in luaguages:
            print(name.title() + "'s favorite number is " + luaguage.title())
    else: 
        print("\n" + name.title() + "'s favorite luaguage are:")
        for luaguage in luaguages:
            print("\t" + luaguage.title())