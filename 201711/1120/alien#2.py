# 创建一个用于储存外星人的空列表
aliens = []

# 创建30个外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5}
    aliens.append(new_alien)

# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

# 显示创建了多少个外星人
print("\nTotal number of aliens: " + str(len(aliens)))