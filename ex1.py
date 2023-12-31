# 1. Write a Python program to find a list of integers with exactly two occurrences
# of nineteen and at least three occurrences of five. Return True otherwise False.
# Input: [19, 19, 15, 5, 3, 5, 5, 2]
# Output:
# True
# Input: [19, 15, 15, 5, 3, 3, 5, 2]
# Output:
# False
# Input: [19, 19, 5, 5, 5, 5, 5]
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
        return True
    else:
        return False
    
if __name__ == "__main__":
    l1 = [19, 19, 15, 5, 3, 5, 5, 2]
    l2 = [19, 15, 15, 5, 3, 3, 5, 2]
    l3 = [19, 19, 5, 5, 5, 5, 5]
    print(nineteenAndFive(l1))
    print(nineteenAndFive(l2))
    print(nineteenAndFive(l3))



