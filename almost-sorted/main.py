#!/bin/python3

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    sl=-1
    sr=-1
    
    # left and right of first and last drop
    # lower and upper limit values chosen to be outside the range
    # of valid arr[i] values in the problem definition 
    # (0 <= arr[i] <= 1000000)
    lold=lord=-1
    rold=rord=1000001

    drops=0
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            drops += 1
            if drops == 1:
                sl = i-1
                sr,rold = i,arr[i]
                if i > 1:
                    lold = arr[i-2]
            
            sr,lord = i,arr[i-1]
            if i < len(arr)-1:
                rord=arr[i+1]

    if drops == 0:
        print("yes")
    elif arr[sr] >= lold and arr[sr] <= rold and \
         arr[sl] >= lord and arr[sl] <= rord:
        if (drops <= 2):
            print("yes")
            print("swap", sl+1, sr+1)
        elif (drops == sr - sl):
            print("yes")
            print("reverse", sl+1, sr+1)
        else:
            print("no")
    else:
        print("no")
 
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
