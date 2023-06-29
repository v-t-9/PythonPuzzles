#  Write a Python program to rescale and shift numbers in a given list, 
# so that they cover the range [0, 1].
# Input:
l1= [18.5, 17.0, 18.0, 19.0, 18.0]
# Output:
# [0.75, 0.0, 0.5, 1.0, 0.5]
# Input:
l2 = [13.0, 17.0, 17.0, 15.5, 2.94]
# Output:
# [0.7155049786628734, 1.0, 1.0, 0.8933143669985776, 0.0]

def rescale(l):
    res = []
    x = 0
    lower = min(l)
    higher = max(l)
    for i in l:
        if i is lower:
            res.append(0.0)
        elif i is higher:
             res.append(1.0)
        else:
            x = (i - lower) /(higher - lower)
            res.append(x)
    return res


print(rescale(l1))
print(rescale(l2))