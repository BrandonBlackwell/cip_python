# Solution to Leetcode 205: Isomorphic Strings
# Time Complexity: O(n) We look at all the pairs in zip and make a comparison
# Space Complexity: O(n) because we create 2 * the number of chars spaceO(2n) which is O(n)

# function solution
def isIsomorphic(s, t):
    my_dict_s = {}
    my_dict_t = {}
    for c1,c2 in zip(s,t):
        # if that key exists already then we can make the checks
        if c1 in my_dict_s and my_dict_s[c1] != c2 or c2 in my_dict_t and my_dict_t[c2] != c1:
            return False
        # if that char doesnt exist already then we need to add it to our dict's
        my_dict_s[c1] = c2
        my_dict_t[c2] = c1
    return True
# main funtion
def main():
    s = "paper" 
    t = "title"
    res = isIsomorphic(s,t)
    print(res)
if __name__ == '__main__':
    main()