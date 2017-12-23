favorite_luaguages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
    }

"""
if 'erin' not in favorite_luaguage.keys():
    print("Erin,please take our poll!")
"""
"""
for name in sorted(favorite_luaguages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("\nThe following luaguage have been mentioned:")
for luaguage in favorite_luaguages.values():
    print(luaguage.title())
"""

print("\nThe following luaguage have been mentioned:")
for luaguage in set(favorite_luaguages.values()):
    print(luaguage.title())