# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(node1, node2):
            if node1 == node2:
                return True
            
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            if dfs(node1.left, node2.left) and dfs(node1.right, node2.right):
                return True
            
            if dfs(node1.left, node2.right) and dfs(node1.right, node2.left):
                return True
            
            return False
        
        return dfs(root1, root2)
