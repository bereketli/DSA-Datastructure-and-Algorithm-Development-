# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []
        def smallest(node):
            if not node:
                return
            left = smallest(node.left)
            right = smallest(node.right)
            if node:
                self.arr.append(node.val)
            return node
        smallest(root)
        self.arr.sort()
        return self.arr[k-1]
        
