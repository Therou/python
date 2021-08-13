d = {}
with open('/etc/passwd') as f:
    for line in f:
        (key. val) = line.split()
        d[int(key)] = val

print(d)
