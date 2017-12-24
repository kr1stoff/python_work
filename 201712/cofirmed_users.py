# 首先，穿件一个待验证的用户列表
# 和一个用于储存已验证的用户的空列表
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

# 验证每个用户，知道没有未验证的用户为止
# 将每个经过验证的列表都转移到已验证的用户列表中
while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print("Veritying user: " + current_users.title())
    confirmed_users.append(current_users)

# 显示所有已验证的用户
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())