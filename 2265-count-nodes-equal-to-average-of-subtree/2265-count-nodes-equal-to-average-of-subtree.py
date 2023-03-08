# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def average(node):
            if not node:
                return [0, 0]
            left = average(node.left)
            right = average(node.right)
            node_child = [left[0] + right[0] + node.val, left[1] + right[1] + 1]
            if node_child[0] // node_child[1] == node.val:
                self.count += 1
            return node_child
        average(root)
        return self.count
                