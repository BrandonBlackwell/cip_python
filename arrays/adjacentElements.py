def solution(inputArray):
   largestP = 0
   for i in range(len(inputArray)-1):
      #j = i+1
      product = inputArray[i]*inputArray[i+1]
      #print(product)
      if product > largestP:
          largestP = product
          #print(largestP)
   return largestP
def main():
  inputArray = [3, 6, -2, -5, 7, 3]
  print(solution(inputArray))
if __name__=="__main__":
  main()