# Write a Python program to split a string of words separated by commas and 
# spaces into two lists, words and separators.
# Input: "W3resource Python, Exercises"
# Output:
# [['W3resource', 'Python', 'Exercises.'], [' ', ', ']]
# Input: "The dance, held in the school gym, ended at midnight"
# Output:
# [['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'], [' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]
# Input: "The colors in my studyroom are blue, green, and yellow"
# Output:
# [['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow.'], [' ', ' ', ' ', ' ', ' ', ' ', ', ', ', ', ' ']]

def stringsAndSeparators(s):
    sep = []
    for i in s:
        if i == " ":
            sep.append(i)
        if i == ",":
            sep.append(i)
    for i in s:
        x = s.find(",")
    s1 = s[:(x)] + s[(x+1):]
    l = s1.split(" ")
    l1 = [l, sep]
    return l1

if __name__ == "__main__":
    s1 = "W3resource Python, Exercises"
    s2 = "The dance, held in the school gym, ended at midnight"
    s3 = "The colors in my studyroom are blue, green, and yellow"
    print(stringsAndSeparators(s1))
    print(stringsAndSeparators(s2))
    print(stringsAndSeparators(s3))