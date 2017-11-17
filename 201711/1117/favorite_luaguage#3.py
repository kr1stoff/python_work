favorite_luaguage = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil','sarah']
for name in favorite_luaguage.keys():
    print(name.title())

    if name in friends:
        print("  Hi " + name.title() + ", I see your favorite luaguage is " \
              + favorite_luaguage[name].title() + ".")
