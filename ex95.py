# Write a Python program to find a palindrome of a given length containing a given string.
# Input: 
# s1 = "madam"
# n1 = 7
# Output:
# madaadam
# Input: madam , 
# n2 = 6
# Output:
# maddam
# Input: madam , 
# n3 = 5
# Output:
# maaaam
# Input: madam , 
# n4 = 3
# Output:
# maam
# Input: madam ,
# n5 = 2
# Output:
# mm
# Input: madam , 
# n6 = 1
# Output:
# aa

def len_palindrome(s,n):
 res = ""
 leng = n // 2
 for i in range(len(s)):
    if len(res)<leng:
        res = res + s[i]
 if n%2 != 0:
    res = res + "a"

 
 return res + res[::-1]

if __name__ == "__main__":
   s1 = "madam"
   n1 = 7
   n2 = 6
   n3 = 5
   n4 = 3
   n5 = 2
   n6 = 1

   print(len_palindrome(s1,n1))
   print(len_palindrome(s1,n2))
   print(len_palindrome(s1,n3))
   print(len_palindrome(s1,n4))
   print(len_palindrome(s1,n5))
   print(len_palindrome(s1,n6))