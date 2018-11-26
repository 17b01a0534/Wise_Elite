#Hacker Rank
#Sherlock and Permutations

#!/bin/python3

import os
import sys

#npr = (n!) / (n-r)! = (n) * (n-1) *(n-2)*........(n-(r-1))
def get_npr(n, r) :
    product = 1
    while r != 0 :
        product = product * n
        n = n - 1
        r = r - 1
    return product


def get_fact(n) :
    fact = 1
    while n != 0 :
        fact = fact * n
        n = n - 1
    return fact

def solve(n, m):
    N = n + m - 1 #First blank is already filled with 1 i.e., n + m - 1 blanks are available
    #We just need to select only n blanks for n 0's i.e., Ncn or Nc(m-1)
    Ncn = (get_npr(N, n) //get_fact(n)) % (10 ** 9 + 7)
    return Ncn



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()

