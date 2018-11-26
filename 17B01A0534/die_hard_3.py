#Hacker Rank
#Die Hard 3

#!/bin/python3

import os
import sys

#Only 4 main conditions exist
#1. large jug is empty
#2.Small jug is empty
#3.Large jug is full
#4.Small jug is full

def solve(a, b, c):
    flag = 0
    if c == a or c == b :
        return "YES"
    else :
        if a > b :
            l = a #l - Quantity of large jug
            s = b #s - Quantity of small jug
        else :
            l = b
            s = a
        if c > l or (a == b and a != c):
            return "NO"
        small = s 
        large = l - s
        while(large != small) :#if large = small then again same process which means failure
            if large == 0 :
                large = l
            elif small == 0 :
                if large >= s :
                    small = s
                    large = large - small
                else :
                    small = large 
                    large = 0
            elif small == s :
                small = 0
            elif  large == l :
                large = large - (s - small)
                small = s
            if large == c or small == c :
                flag = 1
                return "YES"
        if flag == 0 :
            return "NO"
            


t = int(input())

for t_itr in range(t):
    abc = input().split()

    a = int(abc[0])

    b = int(abc[1])

    c = int(abc[2])

    result = solve(a, b, c)

    print(result)

