# LeetCode 206. Reverse Linked List
# Time Complexity: O(n) because we are looking at every node in the list
# Space Complexity: O(1) no extra space was used
#
#

############    #############    ############     ############     ############     ###########       #########
# Node class
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Function to reverse linked list
def reverseList(head):
    prev = None
    node = head
    if node == None:
        return None
    while node != None:
        next_node = node.next
        node.next = prev
        prev = node
        node = next_node
    return prev       
# Main function
def main():
    # Created nodes
    list_head = Node(1)
    list_node1 = Node(2)
    list_node2 = Node(3)
    list_node3 = Node(4)
    list_node4 = Node(5)
    # Connect nodes
    list_head.next = list_node1
    list_node1.next = list_node2
    list_node2.next = list_node3
    list_node3.next = list_node4
    # Function call to reverse the linked list
    reversedList = reverseList(list_head)
    # print linked list
    node = reversedList
    while node != None:
        print(node.val)
        node = node.next
if __name__ == "__main__":
    main()