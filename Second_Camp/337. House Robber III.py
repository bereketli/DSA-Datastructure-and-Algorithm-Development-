# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def houseRobber(node):
            if not node:
                return (0, 0)
            
            left = houseRobber(node.left)
            right = houseRobber(node.right)
            
            
            with_rob = left[1] + right[1] + node.val
            
            without_rob = max(left[0], left[1]) + max(right[0], right[1])
            
            return (with_rob, without_rob)
        
        result = houseRobber(root)
        return max(result[0], result[1])
