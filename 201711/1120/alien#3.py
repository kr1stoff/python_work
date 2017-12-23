# 创建一个用于储存外星人的空列表
aliens = []

# 创建30个绿色的外星人
for alien_numbers in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 前三个外星人数据更改
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
    
print("...")
print("\nTotal number of aliens: " + str(len(aliens)))