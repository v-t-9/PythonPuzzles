# Write a Python program to find the set of distinct characters in a given string, ignoring case.
# s1 = "HELLO"
# Output:
# ['h', 'o', 'l', 'e']
# s2 = "HelLo"
# Output:
# ['h', 'o', 'l', 'e']
# s3 = "Ignoring case"
# Output:
# ['s', 'n', 'c', 'o', 'e', 'i', 'r', 'g', 'a', ' ']

def distinctCharacters(s):
    se = set(s.lower())
    l = []
    
    for i in se:
        l.append(i)
    return sorted(l)

if __name__ == "__main__":
    s1 = "HELLO"
    s2 = "HelLo"
    s3 = "Ignoring case"
    print(distinctCharacters(s1))
    print(distinctCharacters(s2))
    print(distinctCharacters(s3))