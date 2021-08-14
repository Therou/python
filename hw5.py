while True:
    a = list(map(int, input('Enter positive integers separated by space: ').split()))
    a.sort()
    b = [x for x in range(a[0], a[-1] + 1)]
    a = set(a)
    c = list(a ^ set(b))
    c.sort()
    print(c[0])
