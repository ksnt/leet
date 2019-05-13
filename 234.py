# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        stack = []
        while fast != None and fast.next != None:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        # the num of elements is odd
        if fast != None:
            slow = slow.next
        
        while slow != None:
            top = stack.pop()
            if top != slow.val:
                return False
            slow = slow.next
        return True