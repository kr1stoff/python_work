Kristoff = {
    'first_name': 'xf',
    'last_name': 'meng',
    'age': 24,
    'city': 'DG',
    }
# print(Kristoff)


silin = {
    'first name': 'yl',
    'last name': 'li',
    'age': 7,
    'city': 'GZ',
    }

jiuw = {
    'first name': 'hr',
    'last name': 'li',
    'age':24,
    'city':'harbin',
}

peoples = [jiuw,silin,Kristoff]

for people in peoples:
    # print(people)
    for key,value in people.items():
        print(key.title() + ": " + str(value))
    print("\n")