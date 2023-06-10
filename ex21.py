# Write a Python program to check, for each string in a given list, whether the last character 
# is an isolated letter or not. Return True otherwise False.
# Input:
l1 = ['cat', 'car', 'fear', 'center']
# Output:
# [False, False, False, False]
# Input:
l2 = ['ca t', 'car', 'fea r', 'cente r']
# Output:
# [True, False, True, True]

def isolatedLetter(l):
    res = []
    for i in l:
        if " " in i:
            r = True
        else:
            r = False
            
        res.append(r)
    return res
        
print(isolatedLetter(l1))
print(isolatedLetter(l2))
