#Hacker rank
#ncr table

#!/bin/python3

import os
import sys

# Complete the solve function below.
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

def solve(n):
    List = []
    for r in range((n // 2) + 1) :
        ncr = ((get_npr(n, r)) // get_fact(r)) % int(pow(10, 9))
        List.append(ncr)
    new_List = List[0:]
    List.reverse()
    if n % 2 == 0 :
        new_List.pop()
    new_List.extend(List)
    return new_List

T = int(input())
for i in range(T) :
    n = int(input())
    List = solve(n)
    Str = ' '.join(str(ele) for ele in List)
    print(Str)
    

