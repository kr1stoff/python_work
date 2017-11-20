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

name_list = ['jen','sarah','edward','harry','hermione']
for name in name_list:
    if name not in favorite_luaguages.keys():
        print(name.title() + ",could you join our survey?")
    else:
        print(name.title() + ",thanks for joining us!")
