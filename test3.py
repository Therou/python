users = {}
f = open('/etc/passwd')

for line in f_list:
    users[line] = users.get(line,0) + 1

for key in sorted(users):
    print('{}:{}'.format(key, users[key]))
