# Write a Python program to split a string of words separated by commas and 
# spaces into two lists, words and separators.
# Input: 
s1 = "W3resource Python, Exercises"
# Output:
# [['W3resource', 'Python', 'Exercises.'], [' ', ', ']]
# Input: 
s2 = "The dance, held in the school gym, ended at midnight"
# Output:
# [['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'], [' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]
# Input: 
s3 = "The colors in my studyroom are blue, green, and yellow"
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
    return print(l1)

stringsAndSeparators(s1)
stringsAndSeparators(s2)
stringsAndSeparators(s3)