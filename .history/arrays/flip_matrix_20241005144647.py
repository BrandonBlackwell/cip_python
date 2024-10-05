"""Hackerrank Mock Test 1 Week Preperation Kit
Day 2
Mock Test: Flipping Matrix

Given: [[121, 64, 56, 112], [151, 84, 56, 100], [117, 23, 1, 94], [119, 49, 37, 99]]
    112, 49, 56, 121
    94, 56, 84, 100
    117, 23, 1, 151
    119, 64, 37, 99
    
After flipping the matrix.
    Expected:
    121, 64, 56, 112
    151, 84, 56, 100
    117, 23, 1, 94
    119, 49, 37, 99
Return the max sum of first quadrant after flipping the matrix.
Max Sum of the first quadrant is 420
"""
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

def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix)
    l, r = 0, n-1
    t, b = 0, n-1
    max_sum = 0
    
    while t < b:
        for i in range(n//2):
            top_left = matrix[t][l+i]
            top_right = matrix[t][r-i]
            btm_left = matrix[b][l+i]
            btm_right = matrix[b][r-i]
            
            max_val = 0
            j = -1
            k = -1
            exp_max = max(top_left, top_right, btm_left, btm_right)
        
            if top_right == exp_max:
                max_val = top_right
                max_sum += max_val
                j = t
                k = r-i
            elif btm_right == exp_max:
                max_val = btm_right
                max_sum += max_val
                j = b
                k = r-i
            elif btm_left == exp_max:
                max_val = btm_left
                max_sum += max_val
                j = b
                k = l+i
            else:
                max_sum += top_left
            # perform swap
            temp_top_left = top_left
            matrix[t][l+i] = matrix[j][k]
            matrix[j][k] = temp_top_left
        t += 1
        b -= 1
    return max_sum
def reset(matrix: list[list[int]]) -> None:
    matrix.clear()
    matrix.append([112, 49, 56, 121])
    matrix.append([94, 56, 84, 100])
    matrix.append([117, 23, 1, 151])
    matrix.append([119, 64, 37, 99])
   
def main():
    matrix = [[112, 49, 56, 121], [94, 56, 84, 100], [117, 23, 1, 151], [119, 64, 37, 99]]
    print(f"TEST CASE: {matrix}")
    
    result = flippingMatrix(matrix)
    print(f"YOUR OUTPUT: {result}")
    
    # expected = [[121, 64, 56, 112], [151, 84, 56, 100], [117, 23, 1, 94], [119, 49, 37, 99]]
    expected = 420
    print(f"EXPECTED OUTPUT: {expected}")
    
    print(f"Passed testcase: {result==expected}")

    reset(matrix)
    
if __name__ == "__main__":
    main()