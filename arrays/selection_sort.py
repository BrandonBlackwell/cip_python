# Selection Sort Algo
# The key property of selection sort that we want to remember
# is that we want to keep track of the index of the smallest value.
# 1. Loop to iterate to len of list - 1 because we want to stop at
# the index before the last index
# 2. Create variable to store the index of the minimum value
# 3. Create nested loop to iterate over the i+1 items
# 4. Do comparison, if item at j < item at min_index store as min_index
# 5. Swap values AFTER the current iteration finishes
# 
# Time Complexity: O(n^2) because of the nested loops.
# Space Complexity: O(1) because it is an in-place swap therefore, 
# no extra memory is being used.
# =========================================================================
# SELECTION SORT FUNCTION
def selection_sort(array):
    for i in range(len(array)-1):
        min_index = i
        for j in range(i+1,len(array)):
            if array[j]<array[min_index]:
                min_index = j
        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp
    return array
# MAIN FUNCTION
def main():
    my_list = [30,45,10,20,1]
    print(selection_sort(my_list))
    
    
    
if __name__ == "__main__":
    main()