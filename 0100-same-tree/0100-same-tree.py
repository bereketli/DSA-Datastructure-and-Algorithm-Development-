# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same (node1,node2):
            if not node1 or not node2:
                if not node1 and  node2:
                    return False
                elif node1 and not node2:
                    return False
                else:
                    return True
            left = same(node1.left, node2.left)
            right = same(node1.right, node2.right)
            
            return (left and right and node1.val == node2.val)
                
       
        return  same(p, q)
        