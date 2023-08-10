# Given a string consisting of groups of matched nested parentheses separated by parentheses, 
# write a Python program to compute the depth of each group.
# s1 = "(()) (()) () ((()()()))"
# Output:
# [2, 2, 1, 3]
# s2 = "() (()) () () () ()"
# Output:
# [1, 2, 1, 1, 1, 1]
# s3 = "(((((((()))))))) () (()) ((()()()))"
# Output:
# [8, 1, 2, 3]
def depth_nested_parentheses(s):
   l = s.split()
   res = []
   for i in l:
      x = len(i.split(')')[0])
      res.append(x)

   return res
   
  
if __name__ == "__main__":
    s1 = "(()) (()) () ((()()()))"
    s2 = "() (()) () () () ()"
    s3 = "(((((((()))))))) () (()) ((()()()))"

    print(depth_nested_parentheses(s1))
    print(depth_nested_parentheses(s2))
    print(depth_nested_parentheses(s3))