""" 不要再循环外input
pizza_topping = input("\nPlease enter some toppings:")

active = True while active:
    if pizza_topping == 'quit':
        active = False
    else:
        print("We will add " + pizza_topping + "to the pizza.")
"""

""" 原始办法

prompt = "\nPlease enter some toppings:"
topping = ""

while topping != 'quit':
    topping = input(prompt)
    print("We will add " + topping + " to the pizza.")

退出会打印print
""" 

""" 使用标志
prompt = "\nPlease enter some toppings:"

active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
    print("We will add " + topping + " to the pizza.")

使用标志终止程序
""" 

prompt = "\nPlease enter some toppings:"

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("\nWe will add " + topping + " to the pizza.")
    else:
        break

