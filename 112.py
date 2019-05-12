# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        residual = sum - root.val
        if root.left == None and root.right == None and residual == 0:
            return True
        return self.hasPathSum(root.left,residual) or self.hasPathSum(root.right,residual)