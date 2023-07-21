from ex14 import lengthString
# Write a Python program to find the longest string in a given list of strings.
# Input:
l1 = ['cat', 'car', 'fear', 'center']
# Output:
# center
# Input:
l2 = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
# Output:
# shatter

def longestString(l):
    res = lengthString(l)
    maximo = max(res)
    pos = res.index(maximo)
    return l[pos]

if __name__ == "__main__":
    print(longestString(l1))
    print(longestString(l2))