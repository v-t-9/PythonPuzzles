# Write a Python program to find strings in a given list containing a given substring.
# Input:
# [(ca,('cat', 'car', 'fear', 'center'))]
# Output:
# ['cat', 'car']
# Input:
# [(o,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
# Output:
# ['dog', 'donut', 'todo']
# Input:
# [(oe,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
# Output:
# []

def substrInStr(l, substr):
    res = []
    for i in l:
        if substr in i:
            res.append(i)
    return res

if __name__ == "__main__":
    subst1 = "ca"
    l1 = ['cat', 'car', 'fear', 'center']
    subst2 = "o"
    l2 = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
    subst3 = "oe"   
    print(substrInStr(l1, subst1))
    print(substrInStr(l2, subst2))
    print(substrInStr(l2, subst3))
