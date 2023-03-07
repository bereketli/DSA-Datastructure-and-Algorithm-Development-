# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def depth(node):
         
            if not node:
                return 0
            
            left = depth(node.left)
            left += 1
            right = depth(node.right)
            right += 1
            
            return (max(left,right))
       
        return depth(root)
        
        