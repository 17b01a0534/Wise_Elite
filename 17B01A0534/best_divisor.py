#Hacker Rank
#Best Divisor

#!/bin/python3

import math
import os
import random
import re
import sys

def find_factors(n) :
    factors = [1]
    for i in range(2, n) :
        if n % i == 0 :
            factors.append(i)
    factors.append(n)
    return factors

def get_dig_sum(n) :
    Sum = 0
    while n > 0 :
        Sum = Sum + (n % 10)
        n = n // 10
    return Sum

n = int(input())
factors = find_factors(n)
Max = 1
result = 1
for i in range(1, len(factors)) :
    if get_dig_sum(factors[i]) > Max :
        Max = get_dig_sum(factors[i])
        result = factors[i]
print(result)

