# Write a Python program to create a new string by taking a string, and word by word rearranging its characters in ASCII order.
# s1 = "Ascii character table"
# Output:
# Aciis aaccehrrt abelt
# s2 = "maltos won"
# Output:
# almost now

def rearranging_characters(s):
    l = s.split(" ")
    res = ""
    l1 = [sorted(i) for i in l]
    r = ["".join(i) for i in l1]
    res = " ".join(r) 
    return res

if __name__ == "__main__":
    s1 = "Ascii character table"
    s2 = "maltos won"
    print(rearranging_characters(s1))
    print(rearranging_characters(s2))