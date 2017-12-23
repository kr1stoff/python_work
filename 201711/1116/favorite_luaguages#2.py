favorite_luaguages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
    }

"""
# 遍历这个字典
for name,luaguages in favorite_luaguages.items():
    print(name.title() + "'s favorite luaguages is " + luaguages.title() + ".")
"""

# 遍历列表中所有的键
# for name in favorite_luaguages.keys():
for name in favorite_luaguages:
    print(name.title())
