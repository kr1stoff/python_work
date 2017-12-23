favorite_numbers = {
    'silin': [7,8],
    'kristoff': [8,9],
    'jiuw': [28,10],
    'feiy': [10,17],
    'zdpan': [24,24,35],
    }

# 打印每个人最喜欢的数字
for key,values in favorite_numbers.items():
    print("\n" + key.title() + "'s favorite number are: ")
    for value in set(values):
        print("\t" + str(value))