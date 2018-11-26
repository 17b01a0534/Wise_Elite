#Hacker Rank
#Manasa and Factorials


#!/bin/python3

import os
import sys

#Observations
#Ex : No.of 0's in 135 i.e, zeroes_end = (135 // 5) + (135 // 5 ** 2 ) + (135 // 5 ** 3)
#zeroes_end = num * (1/5 + 1/5^2 + 1/5^3 + .... + 1/5^least_expo_5(zeroes_end) )
#From here you can derive a formula for num because elements are in G.P
#Since 135 >= 125(or cube(5))
#No.of 0's at the end of 135 >= 5^0 + 5^1 + 5^2 and <= 5^0 + 5^1 +5^2 + 5^3
#The number You get through the formula is an approx_num

def get_end_0s_in_fact(num) :
    Sum = 0
    while num > 0 :
        num = num // 5
        Sum = Sum + num
    return Sum

def get_approx_num(n) :
    
    res = ((4 * (5 ** least_expo_5(n))) // ((5 ** least_expo_5(n)) - 1)) * n
    return res - (res % 5)

def least_expo_5(n) :
    count = 0
    Sum = 0
    while True :
        Sum = Sum + int(pow(5, count))
        if Sum == n :
            return count + 1
        elif Sum > n :
            return count
        else :
            count += 1

def solve(n):
        approx_num = get_approx_num(n)
        while True :
            if get_end_0s_in_fact(approx_num) >= n :
                return approx_num
            else :
                approx_num += 5

t = int(input())

for t_itr in range(t):
    n = int(input())
    result = solve(n)
    print(result)







