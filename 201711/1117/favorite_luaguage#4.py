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

for name in sorted(favorite_luaguages.keys()):
    print(name.title() + ", thank you for taking the poll.")