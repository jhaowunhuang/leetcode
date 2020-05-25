# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, sum):
        if not root:
            return []
        ans = []

        def func(node, arr, cur_sum):
            if not node.left and not node.right and node.val == cur_sum:
                ans.append(arr + [node.val])
                return
            if node.left:
                func(node.left, arr + [node.val], cur_sum - node.val)
            if node.right:
                func(node.right, arr + [node.val], cur_sum - node.val)
        func(root, [], sum)
        return ans
