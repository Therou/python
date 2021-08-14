input_list = input('asd: ').split()
d = {}
new_list = []
for word in input_list:
    d[word] = d.get(word, 0) + 1

d1 = d
d1.pop(input_list[0])

for k, v in d.items():
    for k1, v1 in d1.items():
        if v > v1:
            print(v, k)
