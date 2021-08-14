total = 0

def bin_convert(n):
    bin1 = bin(n)
    binary = bin1[2:]
    return binary

def palindr(string):
    reverse_string = string[::-1]
    if reverse_string == string:
        return True
    else:
        return False

for i in range(0,1000000):
    val = palindr(str(i))
    binary = bin_convert(i)
    val2 = palindr(str(binary))
    if val == True and val2 == True:
        total = total + i

print(total)
