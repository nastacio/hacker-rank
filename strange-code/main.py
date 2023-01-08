#!/bin/python3

import math
import os

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):
    # cycle : t1 to t2                   value 1
    # 0     : 1 to 3                      3 = 3 * 2^0
    # 1     : 4 to 9                      6 = 3 * 2^1
    # 2     : 10 to 21                   12 = 3 * 2^2
    # 3     : 22 to 45                   24 = 3 * 2^3
    # ...
    # n     : 3*2^^n -2 to 3*2^^n-2 + 3*2^n-1  3 * 2^n
    # n     : 3*2^^n -2 to 3*2^^*(n+1)-3       3 * 2^n
    # n     : 3*2^^n -2 to 6*2^^*n -3          3 * 2^n
    #
    # n     : time + value = t1 in next cycle = 3*2^^(n+1) -2
    n = math.floor(math.log((t+2)/3,2))
    v = 3*2**(n+1)-2 - t
    return v 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
