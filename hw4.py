import re
text = input('Enter integers separated by any symbol: ')
numbers_string = re.findall(r'\d+', text)
numbers_list = [int(i) for i in numbers_string]
sum_of_numbers = sum(numbers_list)
print(sum_of_numbers)
