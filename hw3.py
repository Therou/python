while True:
    input_list = input('enter text: ').lower().split()

    input_list.sort()

    d = {}

    for word in input_list:
        d[word] = d.get(word, 0) + 1

    input_list_second = []

    for i in d.values():
        input_list_second.append(i)

    input_list_second.sort()

    for k, v in d.items():
        if v == max(input_list_second):
            print(v, k)
