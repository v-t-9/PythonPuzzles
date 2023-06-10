# 1. Write a Python program to find a list of integers with exactly two occurrences
# of nineteen and at least three occurrences of five. Return True otherwise False.
# Input:
l1 = [19, 19, 15, 5, 3, 5, 5, 2]
# Output:
# True
# Input:
l2 = [19, 15, 15, 5, 3, 3, 5, 2]
# Output:
# False
# Input:
l3 = [19, 19, 5, 5, 5, 5, 5]
# Output:
# True

def nineteenAndFive(l):
    count19 = 0
    count5 =0
    for i in l:
        if i == 19:
            count19 = count19 + 1
        if i == 5:
            count5 = count5 + 1

    if count19 == 2 and count5 >=3:
        return print(True)
    else:
        return print(False)
    
nineteenAndFive(l1)
nineteenAndFive(l2)
nineteenAndFive(l3)



