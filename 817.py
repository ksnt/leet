# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        G = set(G)
        current = head
        res = 0
        while current:
            if current.val in G:
                if current.next is not None:
                    if current.next.val not in G:
                        res = res + 1
                else:
                    res = res + 1
            current = current.next
        return res