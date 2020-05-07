# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val = 0, left = None, right = None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right and sum == root.val:
            return True
        return self.hasPathSum(root.right, sum - root.val) or self.hasPathSum(root.left, sum - root.val)
