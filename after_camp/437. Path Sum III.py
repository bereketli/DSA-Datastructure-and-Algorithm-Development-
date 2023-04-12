# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.repition = defaultdict(int)
        self.repition[0] = 1
        self.countpath = 0
        def paths(node, prefix):
                if not node:
                   return
                prefix += node.val
                self.countpath += self.repition[prefix - targetSum]
                self.repition[prefix] += 1
                
                left = paths(node.left, prefix)
                if left:
                    self.repition[prefix + left.val] -= 1
                    
                right = paths(node.right, prefix)
                if right:
                    self.repition[prefix + right.val] -= 1
                return node
        paths(root, 0)
        return self.countpath

            
            
        
