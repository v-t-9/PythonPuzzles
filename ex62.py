# Write a Python program to find the dictionary key whose case is different from all other keys.
# Input:
d1 = {'red': '', 'GREEN': '', 'blue': 'orange'}
# Output:
# GREEN
# Input:
d2= {'RED': '', 'GREEN': '', 'orange': '#125GD'}
# Output:
# orange

def dic_key_case(d):
    dic_keys = d.keys()
    lower_case = [ i for i in dic_keys if i.islower()]
    if len(lower_case) == 1:
        return lower_case[0]
    
    upper_case = [ i for i in dic_keys if i.isupper()]
    if len(upper_case) == 1:
        return upper_case[0]

print(dic_key_case(d1))
print(dic_key_case(d2))