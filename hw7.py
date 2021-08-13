users = {}
with open('/etc/passwd') as f:
    for line in f:
        if not line.startswith('#'):
            user_info = line.split(':')
            users[user_info[0]] = user_info[6]


for username in sorted(users):
    shells = '{}'.format(users[username])

shells_list = shells.split()
print(shells_list)
