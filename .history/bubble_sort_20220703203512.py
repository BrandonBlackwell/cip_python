# Bubble Sort Algo
# Start with first item and compare to second item
# If item is larger than second item, switch items
# Repeat process until the end of list is reached.
# Now start process again and compare 
# until 1-end of list is reached

my_list = [6,3,7,5,4,1,2]
#               i
#     j 
for i in range(len(my_list)-1,0,-1):
    for j in range(i):
#This if-statement compares the item at j 
# with the item at j+1.
        if my_list[j] > my_list[j+1]:
            #temp_var holds the item at j
            temp_var = my_list[j]
            # j switches to the item at j+1
            my_list[j] = my_list[j+1]
            #The value that temp_var holds is now stored in j+1 position.
            my_list[j+1] = temp_var
print(my_list)