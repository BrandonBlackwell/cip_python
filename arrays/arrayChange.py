#CodeSignal's "arrayChange"
# Time Complexity: O(n) iterating the length of the inputArray
# Space Complexity: O(1) no extra space is used

# Function Solution
def solution(inputArray):
    # Naive Solution
    # Compare each position 
    # if current position is greater than the prev position
    # then go to next position
    # if current position is less than prev position then inc by 1 and check again 
    # inputArray = [7,4,9,2,7]
    
    # Efficient Solution
    # if current item is less than or equal to prev item
        # get the difference of (prev - curr) + 1 and add the difference to num of moves
        # set current to prev+1
        
    num_of_moves = 0
    i = 1
    while i < len(inputArray):
        curr = i
        prev = i - 1
        if inputArray[curr] <= inputArray[prev]:
            diff = (inputArray[prev]-inputArray[curr])+1
            inputArray[curr] = inputArray[prev]+1
            num_of_moves += diff
        i += 1
            # while inputArray[curr] <= inputArray[prev]:
            #     inputArray[curr] += 1
            #     num_of_moves += 1
            # i += 1
    return num_of_moves
# Main Function
def main():
    arr = [3122, -645, 2616, 13213, -8069]
    result = solution(arr)
    print(result)
if __name__ == "__main__":
    main()