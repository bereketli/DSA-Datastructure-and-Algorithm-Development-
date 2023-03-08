# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.arr = []
        def mode(node):
            if not node:
                return
            left = mode(node.left)
            right = mode(node.right)
            if right:
                self.arr.append(node.val)
            elif left:
                self.arr.append(node.val)
            else:
                 self.arr.append(node.val)
                
            return node
        mode(root)
        
        counted = Counter(self.arr)
        maximum = 0
        for ky in counted:
            maximum = max(maximum, counted[ky])
        output =[]
        for ky in counted:
            if counted[ky] == maximum:
                output.append(ky)
    
            
        return output
        
            