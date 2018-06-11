# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# example
# l1 = ListNode([2,4,3])
# l2 = ListNode([5,6,4])
# sol = Solution()
# so = sol.addTwoNumbers(l1,l2)

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = []
        flag = 0
        while(len(l1.val) != 0):
            if flag == 0:
                if l1.val[-1] + l2.val[-1] >= 10:
                    flag = 1
                    result.append((l1.val.pop() + l2.val.pop()) % 10)
                else:
                    result.append((l1.val.pop() + l2.val.pop()) % 10)
            else:
                if l1.val[-1] + l2.val[-1] >= 10:
                    result.append((l1.val.pop() + l2.val.pop()) % 10 + 1)
                else:
                    flag = 0
                    result.append((l1.val.pop() + l2.val.pop()) % 10 + 1)
        #print(result)
        result.reverse()
        output = ListNode(result)
        #print(output.val)
        return output
