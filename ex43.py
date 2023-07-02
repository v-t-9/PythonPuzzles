# Write a Python program to find all words in a given string with n consonants.
s1 = "this is our time"
# Output:
n1 = 3
# Words in the said string with 3 consonants:
# ['this']
n2 = 2
# Words in the said string with 2 consonants:
# ['time']
n3 = 1
# Words in the said string with 1 consonants:
# ['is', 'our']


def consonants(c):
   if c not in "aeiou":
      return c
  

def numConsonants(s):
  count = 0
  for i in s:
    if consonants(i):
        count = count + 1
  return count

def consString(n, s):
   li = s.split(" ")
   res = []
   for i in li:
    if numConsonants(i) == n:
        res.append(i)
   return res
print(consString(n1, s1))     
print(consString(n2, s1)) 
print(consString(n3, s1)) 




