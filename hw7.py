import sys
shells = []
shells_numbers = {}

with open('/etc/passwd') as f:
    for line in f:
        if not line.startswith('#'):
            user_info = line.split(':')
            shells.append(user_info[6].strip())
            
shells.sort()

for shell in shells:
    shells_numbers[shell] = shells_numbers.get(shell, 0) + 1

sys.stdout = open('output.txt', 'w')
for k, v in shells_numbers.items():
    print(k, '-', v, '; ', end = '')
sys.stdout.close()
