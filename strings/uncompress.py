# Structy Data Structure & Algorithm Course
# Problem: Uncompress
# The function should return an uncompressed version of the string where each 'char' 
# of a group is repeated 'number' times consecutively.

# Solution
# Time Complexity: O(n*m) The number of groups times the maximum number found in any group. ""join is also linear.
# Space Complexity: O(n*m) We create an arr of n*m
def uncompress(s):
  res = []
  i = 0
  j = 0
  while i<len(s) and j<len(s):
    if s[j].isalpha():
      for _ in range(int(s[i:j])):
        res.append(s[j])
      i = j+1
    j+=1
  return "".join(res)

# Main function
def main():
    # Test Cases
    # "2c3a1t"
    # "4s2b"
    # "2p1o5p"
    # "3n12e2z"
    result = uncompress("3n12e2z") # expected output -> 'nnneeeeeeeeeeeezz'
    print(result)
if __name__ == "__main__":
    main()