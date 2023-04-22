# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.grandchild = 0
        def dfs(node):
            if not node:
                return
            left = dfs(node.left)
            right = dfs(node.right)
            if node.val % 2 == 0 :
                if left:
                    if left.left:
                        self.grandchild += left.left.val
                    if left.right:
                        self.grandchild += left.right.val
                if right:
                    if right.left:
                        self.grandchild += right.left.val
                    if right.right:
                        self.grandchild += right.right.val
            return node
        dfs(root)   
        return self.grandchild         
        
