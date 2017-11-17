favorite_luaguage = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
    }

"""
# 遍历这个字典
for name,luaguage in favorite_luaguage.items():
    print(name.title() + "'s favorite luaguage is " + luaguage.title() + ".")
"""

# 遍历列表中所有的键
# for name in favorite_luaguage.keys():
for name in favorite_luaguage:
    print(name.title())
