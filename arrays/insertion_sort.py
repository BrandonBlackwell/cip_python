# Insertion Sort 
    # more efficient than selection sort and bubble sort
    # In place Solution
# =========================================================
# Insertion Sort Algo
    # Array will be divided into 2 sublist, sorted and unsorted
    # Goes from left to right comparing the items that have been seen
    # Sorted will have a length of 1, rest of items will go in unsorted
    # Take the leftmost item from unsorted and put in sorted
    # Compare it to the value to its immediate left
    # If the item to it's immediate left is higher than our current item then swap items
    # continue comparing items to its left until we find an 
    # item less than our current item and the j iterator is less than 0.
    # Then continue to next iteration repeating this process
    # until there are no more items in the unsorted list 
# =========================================================
# Time Complexity:
    # Best Case O(n) When list is sorted or almost sorted
    # Worse Case O(n^2)
# Space Complexity:
    # O(1) because it is sorted in place and does 
    # not use any extra memory.
#===========================================================

# Insertion Sort Function
def insertion_sort(array):
    # Start at index 1 and loop to end of list
    for i in range(1,len(array)):
        # Create var to hold the value of the current item 
        current = array[i]
        # Create iterator that is the value to the left of the i iterator
        j = i - 1
        # Keep executing loop as long as the j iter is > or = 0 and as long as the item at the j index is greater than the current item.
        while j >= 0 and array[j] > current:
            # Perform Swap
            array[j+1] = array[j]
            array[j] = current
            j -= 1
    return array
            
# MAIN Function            
def main():
    my_list = [5,9,3,1,4,7]
    print(insertion_sort(my_list))
    
    
    
if __name__ == '__main__':
    main()



