# Code Signal's - Matrix elements sum
# Expected output: 9
#
#
# Time Complexity: O(m x n) where is m is the number of rows and n is the number of columns. We loop through 
# two 2d Arrays so, 2m x 2n. Drop the constants to get O(m x n).
# Space Complexity: O(m x n) because we create an extra 2d array. 


# Function Solution
def solution(matrix):
    # TRANSPOSE MATRIX
    # This will be the len of each list inside my new list
    row = len(matrix)
    # This will be the len of my new list
    len_of_list = len(matrix[0])
    new_list = []
    #                       Array:position
    # Indexing positions = [0 1 2:0, 1:0 1 2, 2:0 1 2, 3:0 1 2]
    for position in range(len_of_list): # 0 1 2 3
    # Creates an individual list
        nested_list = list()
        for arr in range(row): # 0 1 2 
            nested_list.append(matrix[arr][position])
        new_list.append(nested_list)
    print(new_list)
    # This adds all the items to tot and breaks out the current for loop when the val is 0
    tot = 0
    for arr in new_list:
        for val in arr:
            if val == 0:
                break
            tot += val
    return tot
    #                   BAD SOLUTION 8 OUT OF 10 CORRECT
        # bad_vals = 0
        # bad_vals_arr = []
        # for arr_index, arr in enumerate(matrix):
        #     for item_index, item in enumerate(arr):
                
        #         above = arr_index - 1
        #         # This will ignore items in the first array (the 0th array)
        #         if above > 0:
        #             if matrix[above][item_index] == 0 or matrix[above-1][item_index] == 0:
        #                     bad_vals += item
        #                     bad_vals_arr.append((arr_index,item_index,item))
        # print(bad_vals)
        # print(bad_vals_arr)
        # # Gets total
        # tot = 0
        # for arr in matrix:
        #     for num in arr:
        #         tot += num
        # print(tot)
        # return tot-bad_vals
                
    
            
                
                
    #return tot_sum
# [(i,j),(i,j),(i,j),(i,j)
#  (0,0),(0,1),(0,2),(0,3),
#  (1,0),(1,1),(1,2),(1,3),
#  (2,0),(2,1),(2,2),(2,3)
# ]

# main function
def main():
    matrix = [[0,1,1,2], [0,5,0,0], [2,0,3,3]]
    # function call
    res = solution(matrix)
    print(res)
if __name__ == "__main__":
    main()