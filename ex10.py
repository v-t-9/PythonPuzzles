# 10. Given a string consisting of whitespace and groups of matched parentheses, write a Python program to split it into groups of perfectly matched parentheses without any whitespace.
# Input:
s1 = "( ()) ((()()())) (()) ()"
# Output:
# ['(())', '((()()()))', '(())', '()']
# Input:
s2 = "() (( ( )() ( )) ) ( ())"
# Output:
# ['()', '((()()()))', '(())']
def eraseWhitespace(s):
    l = []
    st=""
    for i in s.replace(" ", ""):
        st = st + i
        if st.count("(") == st.count(")"):
            l.append(st)
            st = ""
    return l

if __name__ == "__main__":
    print(eraseWhitespace(s1))
    print(eraseWhitespace(s2))

