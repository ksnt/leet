# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        current = head
        previous = None
        while current is not None:
        	if current.value == val:
        		if previous is None: # to be deleted node is the element of head
        		    newhead = current.next
        		    current.next = None
        		    return newhead
        		previous.next = current.next
        		return head
        	#update
        	previous = current
        	current = current.next
        return head # not found