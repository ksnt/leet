# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isMirror(self,t1: TreeNode, t2: TreeNode) -> bool:
        if t1 == None and t2 == None:
            return True
        if t1 == None or t2 == None:
            return False
        return (t1.val == t2.val) and self.isMirror(t1.left,t2.right) and self.isMirror(t1.right, t2.left)