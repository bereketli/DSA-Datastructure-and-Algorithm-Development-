# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.forrest = []
        self.delete = []
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.forrest = []
        self.delete = [False] * 1001
        for i in to_delete:
            self.delete[i] = True
        if not self.dfs(root):
            self.forrest.append(root)
        return self.forrest

    def dfs(self, root):
        if root is None:
            return True
        if self.dfs(root.left):
            root.left = None
        if self.dfs(root.right):
            root.right = None
        if self.delete[root.val]:
            if root.left is not None:
                self.forrest.append(root.left)
            if root.right is not None:
                self.forrest.append(root.right)
            return True
        return False
        