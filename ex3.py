# Write a Python program that accepts an integer and determines whether it is 
# greater than 4^4 (4**4) and in which the integer mod 34 == 4.
# Input: 922
# Output:
# True
# Input: 914
# Output:
# False
# Input: 854
# Output:
# True

def expAndReminder(n):
    if n > 4**4 and n % 34 == 4:
        return True
    else:
        return False

if __name__ == "__main__":
   n1 = 922
   n2 = 914
   n3 = 854
   print(expAndReminder(n1))
   print(expAndReminder(n2))
   print(expAndReminder(n3))
