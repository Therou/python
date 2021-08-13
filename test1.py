a =[1,2,3,4,5,7,9,10]
b = [x for x in range(a[0], a[-1] + 1)]
a = set(a)
numbers_list_out_from_input_list = list(a ^ set(b))
numbers_list_out_from_input_list.sort()
print(numbers_list_out_from_input_list[0])
