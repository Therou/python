from collections import Counter
frequent_word = ''
frequency = 0
words = []
input_list = input('Enter text: ').split()
for w in input_list:
    words.append(w)

for i in range(0, len(words)):
    count = 1
    for j in range(i + 1, len(words)):
        if (words[i] == words[j]):
            count = count + 1
    if (count > frequency):
        frequency = count
        frequent_word = words[i]

print(frequency, frequent_word)
