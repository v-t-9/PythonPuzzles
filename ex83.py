# A string is happy if every three consecutive characters are distinct. 
# Write a Python program to find two indices associated with a given string being unhappy.
# Input:
s1 = "Python"
# Output:
# None
# Input:
s2 =  "Unhappy"
# Output:
# [4, 5]
# Input:
s3 = "Find"
# Output:
# None
# Input:
s4 = "Street"
# Output:
# [3, 4]

def happy_unhappy(s):
    res = []
    for i in range(len(s) - 2):
        if s[i] == s[i+1]:
            res.append(i)
            res.append(i+1)
            return res
        if s[i] == s[i+2]:
            res.append(i)
            res.append(i+2)
            return res
        if s[i+1] == s[i+2]:
            res.append(i+1)
            res.append(i+2)
            return res
     

if __name__ == "__main__":
    print(happy_unhappy(s1))
    print(happy_unhappy(s2))
    print(happy_unhappy(s3))
    print(happy_unhappy(s4))
