# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestore = None
        def commonAncestor(node):
            nonlocal ancestore
            if not node:
                return
            if node.val <= max(p.val, q.val) and node.val >= min(p.val, q.val):
                ancestore = node
                return
            elif node.val > max(p.val, q.val):
                 left = commonAncestor(node.left)
            elif node.val < min(p.val, q.val):
                right = commonAncestor(node.right)
            return
        commonAncestor(root)
        return ancestore
