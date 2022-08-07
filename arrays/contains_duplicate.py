def containsDuplicate(nums):
    # SOLUTION 1
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    #   resArr = []
    #   for i in range(len(nums)-1):
    #       for j in range(i+1,len(nums)):
    #           if nums[i] == nums[j]:
    #               resArr.append(True)
    #           else:
    #               resArr.append(False)
    #   for i in resArr:
    #       if i == True:
    #           return True
    #   return False
    ######################################################################################################################################################################
    # SOLUTION 2
    # Uses a dictionary to track the occurrences. If an occurrence is more than 1 true is returned otherwise if there is only 1 occurr of every val then return false
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    myDict = {}
    for i in range(len(nums)):
        if nums[i] in myDict:
            myDict[nums[i]] += 1
            return True
        myDict[nums[i]] = 1
    return False


def main():
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(containsDuplicate(nums))


if __name__ == "__main__":
    main()
