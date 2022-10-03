# LeetCode 896. Monotonic Array
# An array is monotonic if it is either monotone increasing or monotone decreasing.
# Example 1:
# Input: nums = [1,2,2,3]
# Output: true
# Example 2:
# Input: nums = [6,5,4,4]
# Output: true
# Example 3:
# Input: nums = [1,3,2]
# Output: false
#********************************************************************************
# Time Complexity: O(N), the min function takes O(N) and we have to check every item in arr to see if its inc or dec.
# Space Complexity: O(1), no extra space is needed
#********************************************************************************
# solution
def isMonotonic(nums):
#         Get min value
    mini = min(nums)

    #         Items must be increasing, so if there is ever a comparison that is decr return False
    if nums[0] == mini:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return False
        return True
    #         Items must be decreasing, so if there is ever a comparison that is incr return False
    else:
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                return False
        return True
# main function
def main():
    nums = [1,2,2,3]
    result = isMonotonic(nums)
    print(result)
if __name__ == "__main__":
    main()