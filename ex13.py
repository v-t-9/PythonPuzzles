#  Write a Python program to find strings in a given list starting with a given prefix.
# Input:
# [( ca,('cat', 'car', 'fear', 'center'))]
# Output:
# ['cat', 'car']
# Input:
# [(do,('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
# Output:
# ['dog', 'donut']
p1 = "ca"
l1 = ['cat', 'car', 'fear', 'center']
p2 = "do"
l2 = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo']

def stringList(l, p):
    res = []
    for i in l:
        if i.startswith(p):
            res.append(i)
    return res

if __name__ == "__main__":      
    print(stringList(l1,p1))
    print(stringList(l2,p2))