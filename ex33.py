#  Write a Python program to find the positions of all uppercase vowels (not counting Y) in even indices of a given string.
s1 = "w3rEsOUrcE"
# Output:
# [6]
s2 = "AEIOUYW"
# Output:
# [0, 2, 4]

def upperEven(s):
    res = []
    for i in range(len(s)):
        if s[i] is "A" or s[i] is "E" or s[i] is "I" or s[i] is "O" or s[i] is "U":
            if i % 2 == 0:
                res.append(i)
    return res
print(upperEven(s1))
print(upperEven(s2))
