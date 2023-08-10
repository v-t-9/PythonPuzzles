# Write a Python program to find the index of the matching parentheses for each character in a given string.
# s1 = "()(())"
# Output:
# [1, 0, 5, 4, 3, 2]
# s2 = "()()()"
# Output:
# [1, 0, 3, 2, 5, 4]
# s3 = "((()))"
# Output:
# [5, 4, 3, 2, 1, 0]

def matching_parentheses(s):
    res = list(s) 
    x= []
    
    for i in range(len(res)):
        if res[i] == "(":
            x.append(i)
        else:
            res[x[-1]] = i
            res[i] = x.pop()
    return res


if __name__ == "__main__":
    s1 = "()(())"
    s2 = "()()()"
    s3 = "((()))"

    print(matching_parentheses(s1))
    print(matching_parentheses(s2))
    print(matching_parentheses(s3))