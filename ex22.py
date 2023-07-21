# Write a Python program to compute the sum of the ASCII values 
# of the upper-case characters in a given string.
# Input:
s1 = "PytHon ExerciSEs"
# Output:
# 373
# Input:
s2 = "JavaScript"
# Output:
# 157

def sumASCII(s):
    res = 0
    for i in s:
        if i.isupper():
            res = res + ord(i)
    return res

if __name__ == "__main__":
    print(sumASCII(s1))
    print(sumASCII(s2))

