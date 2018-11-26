#Hacker Rank
#Manasa Loves Maths

#!/bin/python3

import os
import sys
from itertools import permutations

# Complete the solve function below.
def solve(n):
    n_str = str(n)
    if len(str(n)) == 1 :
        if n % 8 == 0 :
            return"YES"
        else :
            return "NO"
    elif len(str(n)) == 2 :
        if n % 8 == 0 :
            return "YES"
        elif int(n_str[::-1]) % 8 == 0 :
            return "YES"
        else :
            return "NO"
    perm = permutations(str(n), 3)
    for i in list(perm) :
        Str = ''.join(i)
        j = int(Str)
        if j % 8 == 0 :
            return "YES"
    return "NO"

t = int(input())

for t_itr in range(t):
    n = int(input())

    result = solve(n)

    print(result)


