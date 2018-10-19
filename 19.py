# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head
        while first is not None:
            length = length + 1
            first = first.next
        length = length - n
        first = dummy
        while length > 0:
            length = length - 1
            first = first.next
        first.next = first.next.next
        return dummy.next
        