# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self,head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return None
        t1 = head
        t2 = head.next
        while t2:
            if t1.val == t2.val:
                t1.next = t2.next
            else:
                t1 = t1.next
            t2 = t2.next
        return head