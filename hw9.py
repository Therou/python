# problem 9
print([a * b * (1000 - a - b) for a in range(1, 1000) for b in range(a, 1000) if (1000 - a - b) > 0 if ((1000 - a - b) * (1000 - a - b)) == (a * a + b * b)])

# problem 6
print((sum(range(1, 101)) * sum(range(1, 101))) - sum(i * i for i in range(1, 101)))

#problem 48
print(' '.join(str([(0 + i**i) for i in range(1, 1001)]))[-10:])
#print([(0 + pow(x,x)) % pow(10, 10) for x in range(1, 1001)])
#print([a for a in range(3, 1000) for b in range(a + 1, 999) if (1000 - a - b) > 0 if ((1000 - a - b) * (1000 - a - b)) == (a * a + b * b)])
