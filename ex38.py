# Write a Python program to sort the numbers in a given list by the sum of their digits.
l1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Output:
# [10, 11, 20, 12, 13, 14, 15, 16, 17, 18, 19]
l2 = [23, 2, 9, 34, 8, 9, 10, 74]
# Output:
# [10, 2, 23, 34, 8, 9, 9, 74]

def sumOfDigits(num):
    li = map(int, str(num))
    return sum(li)

def sortedList(l):
    result = sorted(l, key = sumOfDigits)
    return result

print(sortedList(l1))
print(sortedList(l2))
