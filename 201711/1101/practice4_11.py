my_pizzas = ['durian pizza','seafood pizza','pepperoni pizza']
friend_pizzas = my_pizzas[:]

my_pizzas.insert(0,'supreme pizza')
friend_pizzas.insert(0,'super beef pizza')

print ("My favorite pizzas are:")
for pizza_mf in my_pizzas:
    print (pizza_mf.title())

print ("\nMy friend's favorite pizzas are:")
for pizza_ff in friend_pizzas:
    print (pizza_ff.title())