# Write a Python program to shift the decimal digits n places to the left, 
#wrapping the extra digits around. If the shift > the number of digits in n, reverse the string.
# Input:
n1 = 12345 
shift1 = 1
# Output:
# Result = 23451
# Input:
n2 = 12345 
shift2 = 2
# Output:
# Result = 34512
# Input:
n3 = 12345 
shift3 = 3
# Output:
# Result = 45123
# Input:
n4 = 12345 
shift4 = 5
# Output:
# Result = 12345
# Input:
n5 = 12345 
shift5 = 6
# Output:
# Result = 54321

def shift(n,shift):
    s = str(n)
    if shift <= len(s):
        return s[shift:] + s[:shift]
    else:
        return s[::-1]
print(shift(n1,shift1))
print(shift(n2,shift2))
print(shift(n3,shift3))
print(shift(n4,shift4))
print(shift(n5,shift5))
