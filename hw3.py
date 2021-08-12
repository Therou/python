input_text = input('Enter a string: ')
input_dict = {}
for word in input_text.split():
    input_dict[word] = input_dict.get(word,0) + 1

for key in sorted(input_dict):
    print('{} : {}'.format(key,input_dict[key]))
