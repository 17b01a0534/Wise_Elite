#Hacker rank
#Is Fibo

#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(n):
    fib_n_1 = 0
    fib_n_2 = 1
    while True :
        fib_n = fib_n_1 + fib_n_2
        if n == fib_n :
            return "IsFibo"
        elif n > fib_n :
            fib_n_1 = fib_n_2
            fib_n_2 = fib_n
        else :
            return "IsNotFibo"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()

