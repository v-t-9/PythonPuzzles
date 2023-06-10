#  Write a Python program to find the XOR of two given strings interpreted as binary numbers.
# Input:
l1 = ['0001', '1011']
# Output:
# 0b1010
# Input:
l2 = ['100011101100001', '100101100101110']
# Output:
# 0b110001001111

def findXOR(l):
    s1 = l[0]
    n1 = int(s1,2)
    s2 = l[1]
    n2 = int(s2,2)
    res = bin(n1^n2)
    return res
print(findXOR(l1))
print(findXOR(l2))
