while True:
    list_new = input('enter text: ').split()

    list_new.sort()

    d = {}

    for word in list_new:
        d[word] = d.get(word, 0) + 1

    list_new_two = []

    for i in d.values():
        list_new_two.append(i)

    list_new_two.sort()

    for k, v in d.items():
        if v == max(list_new_two):
            print(v, k)
