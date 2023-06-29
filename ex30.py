#  Write a Python program to find a list of strings that have fewer total characters (including repetitions).
# Input:
l1 = [['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]
# Output:
# ['this', 'list', 'is', 'narrow']
# Input:
l2 = [['Red', 'Black', 'Pink'], ['Green', 'Red', 'White']]
# Output:
# ['Red', 'Black', 'Pink']

def fewerTotalChar(l):
    a = int(len(l)/len(l))
    num = []
    c1 = 0
    c2 = 0
    for i in l[:a]:
        for j in i:
            c1 = c1 + len(j)
        num.append(c1)
    for i in l[a:]:
        for j in i:
            c2 = c2 + len(j)
        num.append(c2)
    for i in range(len(num)):
        if min(num):
            return l[i]
print(fewerTotalChar(l1))
print(fewerTotalChar(l2))
