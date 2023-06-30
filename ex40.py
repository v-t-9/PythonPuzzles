# Write a Python program to find strings that, when case is flipped, 
# give a target where vowels are replaced by characters two later.
s1 = "Python"
# Output:
# pYTHQN
s2 = "aeiou"
# Output:
# CGKQW
s3 = "Hello, world!"
# Output:
# hGLLQ, WQRLD!
s4 = "AEIOU"
# Output:
# cgkqw

def flipped(s):
   r = s.swapcase()
   res = []
   st = ""
   for i in r:
      if i == "A" or i == "E" or i == "O" or i == "U" or i == "a" or i == "e" or i == "o" or i == "u":
           c = chr(ord(i) + 2)
           res.append(c)
      else:
        res.append(i)
   return (st.join(res))
print(flipped(s1))
print(flipped(s2))
print(flipped(s3))
print(flipped(s4))