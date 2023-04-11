# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.output = True
      
        def validity(node):
            if not node:
                return 
            left = validity(node.left)
            right = validity(node.right)
            if left and right:
                minimum = min(node.val,left[0], right[0])
                maximum = max(node.val, left[1], right[1])
                if left[1] >= node.val or right[0] <= node.val:
                    self.output = False
            elif  left :
                minimum = min(node.val,left[0])
                maximum = max(node.val, left[1])
                if left[1] >= node.val:
                    self.output = False
            elif right:
                minimum = min(node.val, right[0])
                maximum = max(node.val, right[1])
                if right[0] <= node.val:
                    self.output = False
            else:
                maximum = node.val
                minimum = node.val
            
            return [minimum, maximum]
        validity(root)
        return self.output
                
