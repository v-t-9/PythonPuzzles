from ex60 import Prime
# Write a Python program to find the string consisting of all the words whose 
# lengths are prime numbers.
# Input:
# s1 = "The quick brown fox jumps over the lazy dog."
# Output:
# The quick brown fox jumps the
# Input:
# s2 = "Omicron Effect: Foreign Flights Won't Resume On Dec 15, Decision Later."
# Output:
# Omicron Effect: Foreign Flights Won't On Dec 15,

def str_len_prime(s):
    l =[]
    r = ""
    res = []
    l = s.split(" ")
    leng = list(map(len, l))
    p = Prime(leng)
    for i in range(len(p)):
        if p[i] == True:
            res.append(l[i])
    
    r = " ".join(res)
    return r
if __name__ == "__main__":
    s1 = "The quick brown fox jumps over the lazy dog."
    s2 = "Omicron Effect: Foreign Flights Won't Resume On Dec 15, Decision Later."
    print(str_len_prime(s1))
    print(str_len_prime(s2))