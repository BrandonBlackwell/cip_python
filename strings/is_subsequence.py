# Solution for LeetCode 392
# Time Complexity: O(n) because we are looking at all chars in t and comparing them to s chars.
# Space Complexity: O(1) because we are not creating any extra space

# function solution
def isSubsequence(s,t):
    # Checks for an empty s string
    if s == "":
        return True
    
    # Looks at all chars in t and compares them to s chars. Once we have made the correct num of 
    # Truthy comparisons(which is the len of s) then we know that s is a substring of t so return True 
    # otherwise if we make it to the end and the correct num hasnt been achieved then return False.
    j = 0
    count = 0
    for i in range(len(t)):
        if t[i] == s[j]:
            count += 1
            j += 1
        if count == len(s):
            return True
    return False
# main function
def main():
    s = "abc" 
    t = "ahbgdc"
    res = isSubsequence(s,t)
    print(res)
if __name__ == '__main__':
    main()