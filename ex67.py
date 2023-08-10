# Write a Python program to find a string which, when each character is shifted (ASCII incremented) by shift, gives the result.
# Input:
# s1 = "Ascii character table"
# shift1 = -1
# Output:
# @rbhhbg`q`bsdqs`akd
# Input:
# s2 =  "Ascii character table"
# shift2 = 1
# Output:
# Btdjj!dibsbdufs!ubcmf

def ASCII_incremented(s, shift):
    num = [ord(i) + shift for i in s]
    res = [chr(i) for i in num]
    r = "".join(res)
    return r
if __name__ == "__main__":
    s1 = "Ascii character table"
    shift1 = -1
    s2 =  "Ascii character table"
    shift2 = 1
    print(ASCII_incremented(s1,shift1))
    print(ASCII_incremented(s2,shift2))