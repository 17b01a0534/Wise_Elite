#Hacker rank
#Connecting Towns

#!/bin/python3

import os
import sys

#
# Complete the connectingTowns function below.
#
def connectingTowns(n, routes):
        res = 1;
        for i in range(0, n - 1) :
                res = res * routes[i]
        return res % 1234567
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        routes = list(map(int, input().rstrip().split()))

        result = connectingTowns(n, routes)

        fptr.write(str(result) + '\n')

    fptr.close()

