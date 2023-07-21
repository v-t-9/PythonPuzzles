# Write a Python program to check whether the given strings are palindromes or not. 
# Return True otherwise False.
# Input:
l1 = ['palindrome', 'madamimadam', '', 'foo', 'eyes']
# Output:
# [False, True, True, False, False]
def palindromes(l):
    res = []
    for i in l:
        if i == i[::-1]:
            res.append(True)
        if i != i[::-1]:
            res.append(False)
    return res

if __name__ == "__main__":
    print(palindromes(l1))