# Write a Python program that accepts an integer and determines whether it is 
# greater than 4^4 (4**4) and in which the integer mod 34 == 4.
# Input:
n1 = 922
# Output:
# True
# Input:
n2 = 914
# Output:
# False
# Input:
n3 = 854
# Output:
# True

def expAndReminder(n):
    if n > 4**4 and n % 34 == 4:
        return print(True)
    else:
        return print(False)

expAndReminder(n1)
expAndReminder(n2)
expAndReminder(n3)
