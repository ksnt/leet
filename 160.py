# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        #print(headB.val)
        #return(headB)
        #count = 0
        stackA = []
        stackB = []
        res = None
        while headA:
            stackA.append(headA)
            headA = headA.next
        while headB:
            stackB.append(headB)
            headB = headB.next
        while stackA and stackB:
            topA = stackA.pop()
            topB = stackB.pop()
            if topA == topB:
                res = topA
            else:
                break
        return res