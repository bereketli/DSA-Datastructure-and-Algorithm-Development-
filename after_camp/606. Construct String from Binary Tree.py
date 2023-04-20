# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(arr,node):
            if not node:
                return 
            arr.extend(["(", str(node.val)])
            if not node.left and node.right:
                arr.append("(")
            left = dfs(arr, node.left)
            if not left:
                arr.append(")")
            right =dfs (arr, node.right)
            if left or right:
                arr.append(")")
            return arr
                 

        arr = dfs([], root)
        return "".join((arr[1:len(arr) - 1]))
