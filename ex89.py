from ex60 import Prime
# Write a Python program to find all integers <= 1000 that are the product of exactly three primes. Each integer should be represented as a list of its three prime factors.
# n1 = 10
# Output:
# [[2, 2, 2]]
# n2 = 50
# Output:
# [[2, 2, 2], [2, 2, 3], [2, 2, 5], [2, 2, 7], [2, 2, 11], [2, 3, 2], [2, 3, 3], [2, 3, 5], [2, 3, 7], [2, 5, 2], [2, 5, 3], [2, 5, 5], [2, 7, 2], [2, 7, 3], [2, 11, 2], [3, 2, 2], [3, 2, 3], [3, 2, 5], [3, 2, 7], [3, 3, 2], [3, 3, 3], [3, 3, 5], [3, 5, 2], [3, 5, 3], [3, 7, 2], [5, 2, 2], [5, 2, 3], [5, 2, 5], [5, 3, 2], [5, 3, 3], [5, 5, 2], [7, 2, 2], [7, 2, 3], [7, 3, 2], [11, 2, 2]]

def product_primes(n):
    rj = []
    rk = []
    rl = []
    ri = []
    r = []
    a = [i for i in range(2,n+1)]
    for i in a:
        for j in range(2, n+1):
            for k in range(2, n+1):
                for l in range(2, n+1):
                    if i ==  j * k * l and i not in ri:
                                rj.append(j)
                                rk.append(k)
                                rl.append(l)
                                ri.append(i)
   
    r = list(zip(rj,rk,rl))
    r1 = [list(i)for i in r]
    res = [i for i in r1 if all(Prime(i))]
    return res
                           

if __name__ == "__main__":
    n1 = 10
    n2 = 50
    print(product_primes(n1))
    print(product_primes(n2))