def duplicates_removal(text):
    input_list = []
    [input_list.append(input_text) for input_text in text if input_text not in input_list]
    return input_list

print('Enter any text with words and numbers separated by space:')
input_text = input()

print(" ".join(duplicates_removal(input_text.split())))
