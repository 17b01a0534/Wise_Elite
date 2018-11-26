#Hacker Rank
#Special Multiple

#!/bin/python3

import os
import sys

# Complete the solve function below.
def get_next_multi(prev) :
    next_multi = prev + 1
    Str = ""
    while next_multi > 0 :
        rem = next_multi % 2
        if rem == 1 :
            Str = "9" + Str
        else :
            Str = str(rem) + Str
        next_multi = next_multi // 2
    return Str


def solve(n):
    length = len(str(n))
    multiple = "9" + ("0" * (length - 1))
    dec_value = 2 ** (length - 1)
    if int(multiple) % n == 0 :
        return int(multiple)
    else :
        while True :
            next_multi = get_next_multi(dec_value)
            if int(next_multi) % n == 0 :
                return int(next_multi)
            else :
                dec_value = dec_value + 1
                



t = int(input())

for t_itr in range(t):
    n = int(input())
    result = solve(n)
    print(result)
        

