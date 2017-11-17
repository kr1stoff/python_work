rivers_countries = {
    'nile': 'egypt',
    'yangtzi': 'china',
    'amazon': 'brazil',
    'thames': 'england',
    'mississippi': 'america',
    }

"""
# 用循环为每条河流打印一条消息
for river,country in sorted(rivers_countries.items()):
    print("The " + river.title() + " runs through " + country.title() + ".")
"""

# 用循环把每条河都打印出来
print("\nThe following rivers has been mentioned.")
for river in rivers_countries.keys():
    print(river.title())

# 用循环把每个国家都打印出来
print("\nThe following coutries has been mentioned.")
for country in rivers_countries.values():
    print(country.title())