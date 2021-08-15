import sys
shells = []
shells_numbers = {}
d_user = {}
d_group = {}

with open('passwd') as f:
    for line in f:
        if not line.startswith('#'):
            user_info = line.split(':')
            shells.append(user_info[6].strip())
            d_user[user_info[0]] = user_info[2]

shells.sort()
#print(d_user)

for shell in shells:
    shells_numbers[shell] = shells_numbers.get(shell, 0) + 1

with open('group') as f:
    for line in f:
        if not line.startswith('#'):
            group_info = line.split(':')
            d_group[group_info[0]] = group_info[3]

print(d_group.items())

for k, v in d_user.items():
    for k1, v1 in d_group.items():
        if k in v1:
            print(k1, v)
#print(d_group)
            

sys.stdout = open('output.txt', 'w')
for k, v in shells_numbers.items():
    print(k, '-', v, '; ', end = '')
sys.stdout.close()
