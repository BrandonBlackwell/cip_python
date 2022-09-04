# LeetCode Optimal Solution for Maximum Sum Subarray
# Time Complexity = O(n) because we're walking through all items of the array once.
# Space Complexity = O(1) because we're not using any extra space.

# solution
def maxSubArray(nums):
    # Checks to see if only one item exists in input array
        if len(nums) == 1:
            return nums[0]
        curr_sum = nums[0]
        max_sum = curr_sum
        for i in range(1,len(nums)):
            # current sum will continue to update unless the item that we're on is greater than the current sum
            # then the item will now be the current sum.
            curr_sum = max(curr_sum+nums[i],nums[i])
            # keeps track of the largest sum
            max_sum = max(max_sum,curr_sum)
        return max_sum
# Main function
def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))

if __name__ == "__main__":
    main()