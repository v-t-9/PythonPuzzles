# Write a Python program to find a substring in a given string that contains a vowel between two consonants.
s1 = "Hello"
# Output:
# Hel
s2 = "Sandwhich"
# Output:
# San
s3 = "Python"
# Output:
# hon

def vowel_between_consonants(s):
    vowels = ["a", "e", "i", "o", "u"]
    s1 = ""
    res = []
    for i in range(len(s)):
        if s[i] in vowels:
            s1 = ""
            s1 = s[(i-1):(i+2)]
            if len(s1)==3:
                res.append(s1)

    return res
print(vowel_between_consonants(s1))
print(vowel_between_consonants(s2))
print(vowel_between_consonants(s3))