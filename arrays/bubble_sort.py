# Bubble Sort Algo
# Start with first item and compare to second item
# If item is larger than second item, switch items
# Repeat process until the end of list is reached.
# Now start process again and compare 
# until end of list - 1 is reached



def bubble_sort(some_unordered_list):
    for i in range(len(some_unordered_list)-1,0,-1):
        for j in range(i):
    #This if-statement compares the item at j 
    # with the item at j+1.
            if some_unordered_list[j] > some_unordered_list[j+1]:
                #temp_var holds the item at j
                temp_var = some_unordered_list[j]
                # j switches to the item at j+1
                some_unordered_list[j] = some_unordered_list[j+1]
                #The value that temp_var holds is now stored in j+1 position.
                some_unordered_list[j+1] = temp_var
    return some_unordered_list

my_list = [6,3,7,5,4,1,2]
print(bubble_sort(my_list))
