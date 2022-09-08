# LeetCode 21. Merge Two Sorted Lists
# Time Complexity: O(n) because this is using recursion the call stack will have at most the number of nodes in the lists. We are also 
# comparing them every node.val from both lists
# Space Complexity: O(1) because no extra space was used. 
#
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
##################             #####################             #####################              ###################

# Node class
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2) :
    l1 = list1
    l2 = list2
    if not l1 and not l2:
        # both l1 and l2 are empty list
        return None

    elif not l1:
        # l1 is empty, directly return l2
        return l2

    elif not l2:
        # l2 is empty, directly return l1
        return l1
    if l1.val <= l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l2.next, l1)
        return l2

# Main function
def main():
    # Created nodes
    list1_head = Node(1)
    list1_node1 = Node(2)
    list1_node2 = Node(4)
    # Connect nodes
    list1_head.next = list1_node1
    list1_node1.next = list1_node2
    # Created nodes
    list2_head = Node(1)
    list2_node1 = Node(3)
    list2_node2 = Node(4)
    # Connect nodes
    list2_head.next = list2_node1
    list2_node1.next = list2_node2
    
    # Function call
    final_list = mergeTwoLists(list1_head,list2_head)
    node = final_list
    while node != None:
        print(node.val)
        node = node.next
if __name__ == "__main__":
    main()