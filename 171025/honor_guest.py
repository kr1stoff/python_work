honored_guest = ['jiuwo','dage','erge','yuge']
# 邀请晚餐人数
print (len(honored_guest))

popped_guest = honored_guest.pop(1)
honored_guest.append('achao')
print (popped_guest.title() + " can't come !")
print ("I wanna have a dinner with " + honored_guest[0].title() +"," + honored_guest[1].title() +"," + honored_guest[2].title() +"," + honored_guest[3].title() + "!")

honored_guest.insert(0,'dzj')
honored_guest.insert(2,'qjp')
honored_guest.append('junge')
print ("I wanna have a dinner with " + honored_guest[0].title() +"," + honored_guest[1].title() +"," + honored_guest[2].title() +"," + honored_guest[3].title() +"," + honored_guest[-3].title() +"," + honored_guest[-2].title() +"," + honored_guest[-1].title() + "!")
#一个来不了，后加入两个嘉宾
print(honored_guest)

print ("I just can eat dinnre with two friends!")
popped_guset_1 = honored_guest.pop(0)
print ("I'm sorry, I can't have a dinner with " + popped_guset_1.title() + ".")
popped_guset_2 = honored_guest.pop(1)
print ("I'm sorry, I can't have a dinner with " + popped_guset_2.title() + ".")
popped_guest_3 = honored_guest.pop(1)
print ("I'm sorry, I can't have a dinner with " + popped_guest_3.title() + ".")
popped_guest_4 = honored_guest.pop(-2)
print ("I'm sorry, I can't have a dinner with " + popped_guest_4.title() + ".")
popped_guest_5 = honored_guest.pop(-1)
print ("I'm sorry, I can't have a dinner with " + popped_guest_5.title() + ".")
#pop挑选后的嘉宾列表
print (honored_guest)
# 挑选后邀请晚餐人数
print (len(honored_guest))

print (honored_guest[0].title() + ",i still eat dinner with you!")
print (honored_guest[1].title() + ",i still eat dinner with you!")

del honored_guest[0]
del honored_guest[0]
print (honored_guest)
# 最终人数
print (len(honored_guest))
