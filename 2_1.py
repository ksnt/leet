# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n = ListNode(0)
        flag = 0
        result = []
        while l1 and l2:
            if flag == 0:
                if l1.val + l2.val >= 10:
                    flag = 1
                    n.val += (l1.val + l2.val) % 10
                    result.append(n)
                    n.next = ListNode(0)
                    n = n.next
                    l1,l2 = l1.next, l2.next
                else:
                    n.val += (l1.val + l2.val) % 10
                    result.append(n)
                    n.next = ListNode(0)
                    n = n.next
                    l1,l2 = l1.next, l2.next
            else:
                if l1.val + l2.val >= 10:
                    n.val += (l1.val + l2.val) % 10 + 1
                    result.append(n)
                    n.next = ListNode(0)
                    n = n.next
                    l1,l2 = l1.next, l2.next
                else:
                    flag = 0
                    n.val += (l1.val + l2.val) % 10 + 1
                    result.append(n)
                    n.next = ListNode(0)
                    n = n.next
                    l1,l2 = l1.next, l2.next
        while l1:
            if flag == 0:
                n.val += l1.val
                result.append(n)
                n.next = ListNode(0)
                n = n.next
                l1 = l1.next
            else:
                if l1.val + 1 >= 10:
                    n.val += l1.val + 1
                    result.append(n)
                    n.next = ListNode(0)
                    n = n.next
                    l1 = l1.next
                else:
                    n.val += l1.val + 1
                    flag = 0
                    result.append(n)
                    n.next = ListNode(0)
                    n = n.next
                    l1 = l1.next
        while l2:
            if flag == 0:
                n.val += l2.val
                result.append(n)
                n.next = ListNode(0)
                n = n.next
                l2 = l2.next
            else:
                if l2.val + 1 >= 10:
                    n.val += l2.val + 1
                    result.append(n)
                    n.next = ListNode(0)
                    n = n.next
                    l2 = l2.next
                else:
                    n.val += l2.val + 1
                    flag = 0
                    result.append(n)
                    n.next = ListNode(0)
                    n = n.next
                    l2 = l2.next
        #print(result)
        #print(output.val)
        return n
