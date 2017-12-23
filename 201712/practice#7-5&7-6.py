age_prompt = "\nI will determin the ticket price acconding to your age."
age_prompt += "\nPlease enter 0 to quit!"
age_prompt += "\nHow old are you? "

"""  active
active = True
while active:
    age = input(age_prompt)
    age = int(age)
    if age == 0:
        active = False
    elif  age < 3:
        print("free")
    elif age <= 12:
        print("$10")
    else:
        print("$15")
"""  

""" while条件测试结束循环
age = ""
while  age != 0:
    age = input(age_prompt)
    age = int(age)
    if age < 3:
        print("free") 
    elif age <= 12:
        print("$10")
    else:
        print("$15")
"""
while True:
    age = input(age_prompt)
    age = int(age)
    if age == 0:
        break
    elif age < 3:
        print("free")
    elif age <= 12:
        print("$10")
    else:
        print("$15")
