# Bubble Sort Algo
# Start with first item and compare to second item
# If item is larger than second item, switch items
# Repeat process until the end of list is reached.
# Now start process again and compare 
# until 1-end of list is reached

ul = [6,3,7,5,4,1,2]
for i in range(len(ul)-1,0,-1):
    for j in range(i):
        