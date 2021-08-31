# problem 9
print([a * b * (1000 - a - b) for a in range(1, 1000) for b in range(a, 1000) if (1000 - a - b) > 0 if ((1000 - a - b) * (1000 - a - b)) == (a * a + b * b)])

# problem 6
print((sum(range(1, 101)) * sum(range(1, 101))) - sum(i * i for i in range(1, 101)))

#problem 48
print(sum(pow(n, n) for n in range(1, 1001)) % 10 ** 10)
