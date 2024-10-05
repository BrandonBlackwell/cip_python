# Hackerrank

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix) -> None:
    # Write your code here
    l, r = 0, len(matrix)-1
    t, b = 0, len(matrix)-1
    
    while t<b:
        for i in range(len(matrix)//2):
            t_l = matrix[t][l+i]
            t_r = matrix[t][r-i]
            b_l = matrix[b][l+i]
            b_r = matrix[b][r-i]
            
            max_val = 0
            j = -1
            k = -1
            # top right
            if t_r > t_l and t_r > b_l and t_r > b_r:
                max_val = t_r
                j = t
                k = r-i
            # bottom left
            elif b_l > t_l and  b_l > t_r and b_l > b_r:
                max_val = b_l
                j = b
                k = l+i
            # bottom right
            elif b_r > t_l and b_r > t_r and b_r > b_l:
                max_val = b_r
                j = b
                k = r-i
            temp = t_l
            matrix[t][l+i] = max_val
            matrix[j][k] = temp
        t += 1
        b -= 1

def reset(matrix: list[list[int]]) -> None:
    matrix.clear()
    matrix.append([112, 49, 56, 121])
    matrix.append([94, 56, 84, 100])
    matrix.append([117, 23, 1, 151])
    matrix.append([119, 64, 37, 99])
    
def main():
    matrix = [[112, 49, 56, 121], [94, 56, 84, 100], [117, 23, 1, 151], [119, 64, 37, 99]]
    flippingMatrix(matrix)
    print(f"RESULT: {matrix}")
    
    expected = [[121, 64, 56, 112], [151, 84, 56, 100], [117, 23, 1, 94], [119, 49, 37, 99]]
    print(f"EXPECTED: {expected}")
    """Given:
    112, 49, 56, 121
    94, 56, 84, 100
    117, 23, 1, 151
    119, 64, 37, 99
    
    [[121, 64, 56, 112], [151, 84, 56, 100], [117, 23, 1, 94], [119, 49, 37, 99]]
    Expected:
    121, 64, 56, 112
    151, 84, 56, 100
    117, 23, 1, 94
    119, 49, 37, 99
    """
    reset(matrix)
    print(f"ORIGINAL: {matrix}")
    
if __name__ == "__main__":
    main()