text = input()
input_list = text.split()
frequency_word = ""
frequency = 0

for i in range(0, len(input_list)):
    count = 1
    for j in range(i+1, len(input_list)):
        if(input_list[i] == input_list[j]):
            count = count + 1
    if(count > frequency):
        frequency = count
        frequent_word = input_list[i]

print(str(frequency), frequent_word)
