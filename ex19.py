# Write a Python program to split a given string (s) into strings if there is a space in s, otherwise split on commas if there is a comma, otherwise return the list of lowercase letters in odd order (order of a = 0, b = 1, etc.).
# Input: "a b c d"
# Split the said string into strings if there is a space in the string,
# otherwise split on commas if there is a comma,
# Output:
# ['a', 'b', 'c', 'd']
# Input: "a,b,c,d"
# Split the said string into strings if there is a space in the string,
# otherwise split on commas if there is a comma,
# Output:
# ['a', 'b', 'c', 'd']
# Input: "abcd"
# Split the said string into strings if there is a space in the string,
# otherwise split on commas if there is a comma,
# Output:
# ['b', 'd']

def splitStrings(st):
    res = ""
    if " " in st:
        r = st.split(" ")
        return r
    if "," in st:
        r = st.split(",")
        return r
    for i in range(len(st)):
        if i % 2 != 0:
            res = res + st[i]
            r = list(res)
    return r 

if __name__ == "__main__":
    s1 = "a b c d"
    s2 = "a,b,c,d"
    s3 = "abcd"
    print(splitStrings(s1))
    print(splitStrings(s2))
    print(splitStrings(s3))
