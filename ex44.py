# Write a Python program to find which characters of a hexadecimal number correspond to prime numbers.
s1 = "123ABCD"
# Output:
# [False, True, True, False, True, False, True]
s2 = "123456"
# Output:
# [False, True, True, False, True, False]
s3 = "FACE"
# Output:
# [False, False, False, False]

dict = {
    "A":10,
    "B":11,
    "C":12,
    "D":13,
    "E":14,
    "F":15
}

def Hex(s, dict):
    l = []
    for i in s:
        if i.isdigit():
            l.append(int(i))
        elif i in dict:
             l.append(dict[i])
    return l

def Prime(s = ""):
    h = Hex(s, dict)
    res = []
    for i in h:
        c = 0
        for j in range(1,i):
            if i %j == 0:
                c = c +1
        if c == 1:
            res.append(True)
        else:
            res.append(False)
    return res

print(Prime(s1))
print(Prime(s2))
print(Prime(s3))
