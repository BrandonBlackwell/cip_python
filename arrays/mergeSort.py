#                        MERGE SORT
#
# 1. Sort
# 2. Recurse
# 3. Merge
#                        Big O
# Time Complexity: O(n log(n)) because sorting take log n time because of halving and merging takes n time because we have to put every item back together.
# Space Complexity: O(n) because it creates new lists for each item
# merge sort function
def mergeSort(arr):
    # Sorting (Takes log n time to sort)
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        #print("left ",left,"right ",right)
        
        #recursive calls
        mergeSort(left)
        mergeSort(right)
        
        # Merging (Time it takes putting list back together is O(n))
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
# Main Function            
def main():   
    nums = [8,3,5,9,10,20,50,12,9384,90,101]   
    print("Original Array: ", nums)
    # Function Call
    mergeSort(nums)
    print("Sorted Array: ",nums)
if __name__ == "__main__":
    main()
