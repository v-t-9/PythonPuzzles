# Write a Python program to create a string consisting of non-negative integers up to n inclusive.
# Input:
# 4
# Output:
# 0 1 2 3 4
# Input:
# 15
# Output:
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
n1=4
n2=15
def strToNInclusive(n):
    st = ""
    for i in range(n+1):
        st = st + str(i) + " "
    return st
print(strToNInclusive(n1))
print(strToNInclusive(n2))
    