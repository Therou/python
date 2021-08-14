def duplicates_removal(text):
    input_list = []
    [input_list.append(input_text) for input_text in text if input_text not in input_list]
    return input_list

input_text = input('Enter any text with words and numbers separated by space: ')

print(" ".join(duplicates_removal(input_text.split())))
