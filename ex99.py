# Write a Python program to find a string such that, when three or more spaces are 
# compacted to a '-' and one or two spaces are replaced by underscores, leads to the target.
s1 = "Python-Exercises"
# Output:
# Python Exercises
s2 =  "Python_Exercises"
# Output:
# Python Exercises
s3 = "-Hello,_world!__This_is-so-easy!-"
# Output:
# Hello, world! This is so easy!

def replace_with_spaces(s):

    res = s.replace("-", "   ").replace("_", "  ")
    return res
   
if __name__ == "__main__":
    print(replace_with_spaces(s1))
    print(replace_with_spaces(s2))
    print(replace_with_spaces(s3))
