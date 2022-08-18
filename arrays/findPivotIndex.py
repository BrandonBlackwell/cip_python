def pivotIndex(nums):
    # TESTCASE 1:
    # nums = [1,7,3,6,5,6]
    #               p
    #                   i
    # leftSum = 11 rightSum = 11
    
    # TESTCASE 2: 
    # nums = [2,1,-1]  
    #            p
    #              i
    
    # SOLUTION 1: BRUTE FORCE O(n^2)
    # set pivot to be first item in arr and loop as long as pivot is < len of arr
        # create for loop to sum every item to the right of pivot(rightSum)
            # check if rightSum == leftSum
                # if true then return the pivot index
            # Otherwise, add current pvot item to leftSum and inc pivot by 1 and set rightSum = 0
        # if no pivot is found return -1
    
    # leftSum = 0
    # rightSum = 0
    # p = 0
    # #i = p+1
    # while p < len(nums):
    #     for i in range(p+1,len(nums)):
    #         rightSum += nums[i]
    #     if leftSum == rightSum:
    #         return p
    #     leftSum += nums[p]
    #     rightSum = 0
    #     p+=1
    # return -1
###########################################################################################     
    # SOLUTION 2: O(n)    
# rightSum = tot - pivot item - leftSum
# nums = [1,2,3]
#                   p
#   leftSum = 3 rightSum = 0
# Stored total sum of arr
# Loop as long as pivot index < len of arr
    # compute rightSum by subtracting the leftSum and pivot item from total sum
    # check if rightSum == leftSum
        # if true then return the pivot index
    # Otherwise, add current pvot item to leftSum and inc pivot by 1 and set rightSum = 0
# if no pivot is found return -1
    tot = sum(nums) # O(n) function
    leftSum = 0 # O(1)
    p = 0 # O(1)
    while p < len(nums): # O(n)
        rightSum = tot-nums[p]-leftSum # O(1)
        if leftSum == rightSum: # O(1)
            return p # O(1)
        rightSum = 0 # O(1)
        leftSum += nums[p] # O(1)
        p+=1 # O(1)
    return -1 # O(1)
# Time Complexity: O(n)
    
    
    
    
    
    
    
    
    
#******************* BAD SOLUTION**********************#    
#         mid = len(nums)//2
#         lArr = nums[:mid]
#         rArr = nums[mid:]
#         l = 0
#         r = len(rArr)-1
#         leftSum = 0
#         rightSum = 0
    
    # Keep looping as long as l is less than r
    # while l < r:
    #while l and r and l < r:
        # Check if l and r pointers are out of bounds
        #if l < 0 or l > len(lArr) or r < 0 or r > len(rArr):
        # if len(nums) == 3:
        #     rightSum += rArr[r]
        # elif rightSum < leftSum:
        #     r-=1
        # elif rightSum > leftSum:
        #     leftSum += lArr[l]
        # if leftSum == rightSum:
        #     return 0
        # l+=1
        
#******************* BAD SOLUTION**********************#    
    # leftSum = lArr[l]
    # rightSum = rArr[r]
    # while l != r or l < r:
    #     # leftSum += lArr[l]
    #     # righttSum += rArr[r]
    #     if leftSum == rightSum:
    #         return l+1
    #     elif leftSum < rightSum:
    #         l+=1
    #         leftSum = lArr[l]
    #         #leftSum += lArr[l]
    #     elif rightSum < leftSum:
    #         r-=1
    #         rightSum = rArr[r]
    #         #rightSum += rArr[r]
    # return 