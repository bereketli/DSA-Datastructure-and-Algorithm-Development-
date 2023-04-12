# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.summed = 0
        def sumpath(arr, node):
            if not node:
                return
            arr.append(str(node.val))
            left = sumpath(arr, node.left)
            if left:
                arr.pop()
            right = sumpath(arr, node.right)
            if right:
                arr.pop()
            if not right and not left:
                self.summed += int("".join(arr))
            return node
        sumpath([],root)
        return self.summed

        """
        function(node, arr):
        
        base case :if no node:
        if noleft and right
        concantnate conten of arr and add to the store

        """
