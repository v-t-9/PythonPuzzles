# Write a Python program to reverse the case of all strings. For those strings, which contain 
# no letters, reverse the strings.
# Original list:
l1 = ['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
# Reverse the case of all strings. For those strings which contain no letters, reverse the strings:
# ['CAT', 'CATATATATCTSA', 'ABCDEFHIJKLMNOP', '521581932952421', '', 'FOO', 'UNIQUE']
# Original list:
l2 = ['Green', 'Red', 'Orange', 'Yellow', '', 'White']
# Reverse the case of all strings. For those strings which contain no letters, reverse the strings:
# ['gREEN', 'rED', 'oRANGE', 'yELLOW', '', 'wHITE']
# Original list:
l3 = ['Hello', '!@#', '!@#$', '123#@!']
# Reverse the case of all strings. For those strings which contain no letters, reverse the strings:
# ['hELLO', '#@!', '$#@!', '!@#321']

def reverse_case(l):
    res = []
    for i in l:
        if i.isalpha():
            res.append(i.swapcase())
        else:
            res.append(i[::-1])
    return res
print(reverse_case(l1))
print(reverse_case(l2))
print(reverse_case(l3))