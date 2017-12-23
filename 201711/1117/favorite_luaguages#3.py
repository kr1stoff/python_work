favorite_luaguages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil','sarah']
for name in favorite_luaguages.keys():
    print(name.title())

    if name in friends:
        print("  Hi " + name.title() + ", I see your favorite luaguage is " \
              + favorite_luaguages[name].title() + ".")
