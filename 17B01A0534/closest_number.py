#Hacker Rank
#Closest Number

#!/bin/python3

import os
import sys

#
# Complete the closestNumber function below.
#
def closestNumber(a, b, x):
    #
    # Write your code here.
    #
    a_pow_b = int(pow(a, b))
    multiplier = a_pow_b // x
    res1 = multiplier * x
    res2 = (multiplier + 1) * x
    diff1 = a_pow_b - res1
    diff2 = res2 - a_pow_b
    if(diff1 < diff2) :
        return res1
    elif(diff2 < diff1) :
        return res2
    else :
        return res1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        abx = input().split()

        a = int(abx[0])

        b = int(abx[1])

        x = int(abx[2])

        result = closestNumber(a, b, x)

        fptr.write(str(result) + '\n')

    fptr.close()

