#  Write a Python program to find a valid substring of a given string that contains matching brackets, at least one of which is nested.
# Input:
s1 = "]][][[]]]"
# Output:
# [[]]
# Input:
s2 = "]]]]]]]]]]]]]]]]][][][][]]]]]]]]]]][[[][[][[[[[][][][]][[[[[[[[[[[[[[[[[["
# Output:
# [[][][][]]

# def cons_num(l):
#     r = []
#     while sorted(l) == list(range(min(l), max(l)+1)):
            
#       return r


def nested_str(s):
    a = []
    d = []
    res = []
    l = list(s)
    #######################################################
    i1 = l.index("[")
    rev = list(reversed(l))
    i2 = rev.index("]")
    li = l[i1:len(l)-i2]

    for i in range(len(li)):
         if (li[i-1] == "[" and li[i] == "]") and ((li[i-3] != "[" and li[i-2] != "[")):
              a.append(i-1)
              a.append(i)
    
    b= [li[i] for i in range(len(li)) if i not in a]
   
    for i in range(len(b)):
         if b.count("[") < b.count("]"):
            if b[i] == "]":
                d.append(i)
         
         if b.count("[")>b.count("]"):
              if b[i] == "[":
                d.append(i)
    del b[d[0]]

    res = "".join(b)
    return res

print(nested_str(s1))
print(nested_str(s2))


   

