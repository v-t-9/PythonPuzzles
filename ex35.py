# Write a Python program to compute the product of the odd digits in 
# a given number, or 0 if there aren't any.
n1 = 123456789
# Output:
# 945
n2 = 2468
# Output:
# 0
n3 = 13579
# Output:
# 945

def productOddDigits(n):
    res = 1
    r = 0
    s = str(n)
    for i in s:
        if int(i) % 2 != 0:
            res = res * int(i)
    if res != 1:
        return res
    if res == 1:
        return r  
print(productOddDigits(n1))
print(productOddDigits(n2))
print(productOddDigits(n3))