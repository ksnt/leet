# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getHeight(self,root):
            if root == None:
                return 0
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        heightDiff = self.getHeight(root.left) - self.getHeight(root.right)
        if abs(heightDiff) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)