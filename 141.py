# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seennode = set()
        while head != None:
            if head in seennode:
                return True
            else:
                seennode.add(head)
            head = head.next
        return False