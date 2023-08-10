# Write a Python program to find the closest palindrome to a given string.
# Input:
# s1 = "cat"
# Output:
# cac
# Input:
# s2 = "madan"
# Output:
# madam
# Input:
# s3 = "radivider"
# Output:
# radividar
# Input:
# s4 = "abc"
# Output:
# aba
# Input:
# s5 = "racecbr"
# Output:
# racecar

def closest_palindrome(s):
    res = ""
    mid = int(len(s)/2)
    mb = s[:mid]
    res = res + mb + s[mid] + mb[::-1]

    return res



if __name__ == "__main__":
    s1 = "cat" 
    s2 = "madan"
    s3 = "radivider"
    s4 = "abc"
    s5 = "racecbr"
    print(closest_palindrome(s1))
    print(closest_palindrome(s2))
    print(closest_palindrome(s3))
    print(closest_palindrome(s4))
    print(closest_palindrome(s5))