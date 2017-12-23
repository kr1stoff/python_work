my_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream','cannoli']

print ("The first three items in the list:")
for items in my_foods[:3]:
    print (items.title())

print ("\nThe first three items in the list:")
for items in my_foods[1:4]:
    print (items.title())

print ("\nThe first three items in the list:")
for items in my_foods[-3:]:
    print (items.title())