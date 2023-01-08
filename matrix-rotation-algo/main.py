#!/bin/python3

import math

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

# Converts a linear index of all elements in a rectangle, oriented
# in a clock-wise manner from the upper-left corner.
#
# In other words, imagine a vector containing all elements
# in the rectangle, following the segments in order of
# top, right, bottom, and finally, left.
#
# For example, in a rectangle of 5 rows and 4 columns, an
# index (vector_index) of 6 means getting past all 4 elements in the
# first row (0,1,2,3) and then 2 more elements down the right-side
# of the rectangle (4,5).
# 
# The coordinates should be 2,3
#
def coords(vector_index, rect_cutoff_left, rect_cutoff_bottom, rect_cutoff_right, left_column,right_column,top_row, bottom_row):
    # left segment of rectangle
    if vector_index >= rect_cutoff_left:
        row = bottom_row - (vector_index - rect_cutoff_left)
        column = left_column
    # bottom segment of rectangle
    elif vector_index >= rect_cutoff_bottom:
        row = bottom_row
        column = right_column - (vector_index - rect_cutoff_bottom)
    # right segment of rectangle
    elif vector_index >= rect_cutoff_right:
        row = top_row + (vector_index - rect_cutoff_right)
        column = right_column
    else:
    # top segment of rectangle
        row = top_row
        column = left_column + vector_index
    
    return (row, column)

def matrixRotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])
    
    layers = math.ceil(min(m / 2 , n / 2))

    new_matrix = [[0 for _ in range(n)]  for _ in range(m)]        

    for l in range(layers):
        elements_in_layer = 2*(m-2*l) + 2*(n-2*l) - 4

        # No point in completely rotating a layer multiple times.
        # only rotate the remainder of the last full rotation.
        r1 = r % elements_in_layer

        rect_cutoff_right = n-2*l - 1
        rect_cutoff_bottom = rect_cutoff_right + m-2*l - 1
        rect_cutoff_left = rect_cutoff_bottom + n-2*l - 1
        left_column=l
        right_column=n-l-1
        top_row=l
        bottom_row=m-l-1
        
        # print("cutoffs", rect_cutoff_right, rect_cutoff_bottom, rect_cutoff_left)

        for vector_index in range(elements_in_layer):
            vector_rotated_index = (vector_index + r1) % elements_in_layer

            vector_index_coords = coords(vector_index, rect_cutoff_left, rect_cutoff_bottom, rect_cutoff_right, left_column,right_column,top_row, bottom_row)            
            vector_index_row = vector_index_coords[0]
            vector_index_column = vector_index_coords[1]

            vector_rotated_index_coords = coords(vector_rotated_index, rect_cutoff_left, rect_cutoff_bottom, rect_cutoff_right, left_column,right_column,top_row, bottom_row)            
            vector_rotated_index_row = vector_rotated_index_coords[0]
            vector_rotated_index_column = vector_rotated_index_coords[1]

            # print("e", e, (e_row, e_column), "e1", e1, (e1_row, e1_column))
            new_matrix[vector_index_row][vector_index_column] = matrix[vector_rotated_index_row][vector_rotated_index_column]
    
    [ print(*new_matrix[mi]) for mi in range(m) ]

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
