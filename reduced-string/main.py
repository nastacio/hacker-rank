#!/bin/python3

import os
from functools import reduce 

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

# def reduce_string(reduced_string, next_char):
#     if len(reduced_string) > 0 and reduced_string[-1] == next_char:
#         reduced_string[:-1]
#     else:
#         reduced_string + next_char

def superReducedString(s):
    # result = reduce(reduce_string , s)
    remove_dup_chars = lambda x,y: x[:-1] if len(x) > 0 and x[-1] == y else x + y
    result = reduce(remove_dup_chars, s)
    return result if len(result) > 0 else "Empty String"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
