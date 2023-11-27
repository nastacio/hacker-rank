#!/bin/python3

# https://www.hackerrank.com/challenges/countingsort4/problem?isFullScreen=true

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    d = {}
    arr_mid = len(arr)/2
    for index, a in enumerate(arr):
        k = int(a[0])
        v = "-" if index < arr_mid else a[1]
        if k in d.keys():
            d[k].append(v)
        else:
            d[k] = [v]

    r = ""
    for sk in sorted(d.keys()):
        r = " ".join([r, *d[sk]])
    print(r.strip())


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
