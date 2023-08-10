# Write a Python program to find a string consisting of space-separated characters with given counts.
# d1 ={'f': 1, 'o': 2}
# Output:
# f o o
# d2 = {'a': 1, 'b': 1, 'c': 1}
# Output:
# a b c

def string_space_separated_characters(d):
    key = d.keys()
    r = " "
    res = " "
    for i in key:
        r = r + d[i]*i 
    for i in r:
        res = res + i + " "
    return res

if __name__ == "__main__":
    d1 ={'f': 1, 'o': 2}
    d2 = {'a': 1, 'b': 1, 'c': 1}

    print(string_space_separated_characters(d1))
    print(string_space_separated_characters(d2))