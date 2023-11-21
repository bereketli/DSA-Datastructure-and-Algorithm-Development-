# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.summed = 0
        def dfs(node):
            if not node:
                return None
            if not node.left and not node.right:
                return "leaf"
            left = dfs(node.left)
            if left == "leaf":
                self.summed += node.left.val
            dfs(node.right)
        dfs(root)
        return self.summed