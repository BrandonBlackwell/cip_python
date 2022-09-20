# Code Signal's common char count
# Time Complexity: O(n log n) after droping all the constants
# Space Complexity:  O(n) <- O(2n) -> two dict's are created so that would be 2 x the number of items in s1(n represents the number of items)
########################################
# ALGORITHM
# Sort s1 and s2
# Get char count of s1 and s2
# Get the smallest char count val from each similar val and store in arr
# Accumulate all vals in arr
# s1: "abcdefghxyzttw"
# s2: "hgfedcbaabcwwt"
# WALKTHROUGH
# a b c d e f g h t w
# 1 1 1 1 1 1 1 1 2 1
# a b c d e f g h t w
# 2 2 2 1 1 1 1 1 1 2
# accumulator = 1+1+1+1+1+1+1+1+1+1 = 10
def solution(s1, s2):
    s1 = sorted(s1) # T:O(n log n) worst case, S: O(1) returns 1 new string
    s2 = sorted(s2) # T:O(n log n) worst case, S: O(1) returns 1 new string
    my_dict1 = dict() # T:O(1) S:O(n the number of chars in s1 at worst)
    my_dict2 = dict() # T:O(1) S:O(n the number of chars in s2 at worst)
    for i in s1: # T:O(n) S:O(n) adding all items to dict1 at worst case 
        if i in s2:
            if i not in my_dict1:
                my_dict1[i] = 1
            else:
                my_dict1[i] += 1
    for i in s2: # T: O(n) S:O(n) adding all items to dict2 at worst case 
        if i in s1:
            if i not in my_dict2:
                my_dict2[i] = 1
            else:
                my_dict2[i] += 1
    accumulator = 0
    for v1, v2 in zip(my_dict1.values(),my_dict2.values()): # for loop T: O(n), zip() runs O(n). Total for this line is O(2xn)
       accumulator += min(v1,v2)
    return accumulator
# main function
def main():
    string1,string2 = "abcdefghtw","abcdefghtw"
    result = solution(string1,string2)
    print(result)
if __name__ == "__main__":
    main()
