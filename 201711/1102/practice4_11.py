my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print ("My favorite foods are:")
for food_mf in my_foods:
    print (food_mf.title())

print ("\nMy friend favorite foods are:")
for food_ff in friend_foods:
    print (food_ff.title())
