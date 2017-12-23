our_favorite_info = {
    'silin': {
        'color': 'blue',
        'numbers': [7,8],
        },    
    'kristoff': {
        'color': 'pink',
        'numbers': [8,9],
        },
    'jiuw': {
        'color': 'pink',
        'numbers': [10,27],
        },
    'zdpan':{
        'color': 'black',
        'numbers': [24,35],
        }, 
    }

"""
print(our_favorite_info.keys())
print(our_favorite_info.values())
"""
# 遍历 our_f avorite_info 中的小字典，key为小字典名，value为小字典的键-值对
for key_n,info in our_favorite_info.items():
    print("\n" + key_n)
    for key_t,value in info.items():
# 数字列表/元素，要加str     
        print("\t" + key_t.title() + ": " + str(value))