# The rotation of a linked list can be defined as an operation that makes a node k 
# the new head of the linked list, and appends each element that was before k to the 
# end of the linked list. We can call the element selected the kth element of the linked 
# list, and thus call the resulting linked list the kth rotation. 

# Write a function, which takes a Node and an integer k as it’s arguments and returns a new 
# node that is the head of the kth rotation of the linked list. If the value k is longer than 
# the length of the linked list, is 0, or is negative, instead return the original linked list. 
# If the Node is None, return None. You will not be passed a circular linked list.
# You are guaranteed the linked list will have no more than 1,000,000 nodes.

"""
Joseph Wu
CMSC389O section 0301
uid: 118956183
I pledge on my honor that I have not given or received any unauthorized 
assistance on this assignment/examination.

The problem my code solves: 
My code rotates a linked list so that a section of the linked list is moved 
back and the nodes of that section are still in order. Real world 
applications of this include: rotating a queue of tasks, shifting music 
playlist queues, storing browsing history, etc.

How does my code work?
My code first goes through the linked list to find the length and set the 
tail node. Then, I iterate to the kth node to set that as the new head. I 
also append the linked list in the process by setting the tail node's next 
to original head. I also check the edge cases where head is None and the 
value k is not valid (less than 0 or greater than the length of the list). 


Time Complexity:
My code has a time complexity of O(n). It takes constant time to declare the
variables, do the if statement checks and return list. I iterate through the
whole list once in the while loop, taking n time. I also iterate k times in 
the for loop which will take at most n time. This is at most a total of 2n 
plus some constant which is O(n) time.

Auxillary Space Analysis:
This code takes up O(1) space. The variables created to perform this 
calcuation are curr, tail, length, and new_head. These are variables that 
remain constant regardless of how long the list is making them some 
constant space. No recursion or extra data structures were made that 
would be dependent on list size. This makes it Auxillary Space of O(1).
"""

class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

def rotate_list(head: 'Node', k: int) -> 'Node':
    #checks validity of passed in values: if list exists and if k is negative
    if head is None or k <= 0:
        return head

    #declare variables
    curr = head     #used to get to kth node
    tail = head     #used to get the tail node
    length = 1      #used to find length of linked list

    #find the length of the list and set tail to last node
    while tail.next is not None:
        tail = tail.next
        length += 1
    
    #checks if k is too long to perform rotating operation
    if k >= length:
        return head
    
    #get to k node
    for i in range(k - 1):
        curr = curr.next
    #set up the new list with kth node as the head and appending
    new_head = curr.next
    curr.next = None
    tail.next = head

    return new_head


