current_users = ['kristoff','xfmeng','zdpan','silin','byu','zxzheng']
new_users = ['KRISTOFF','jiuwo','yuge','junge','xfmeng']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Need to input other user name.")
    else:
        print("User name not registed.")