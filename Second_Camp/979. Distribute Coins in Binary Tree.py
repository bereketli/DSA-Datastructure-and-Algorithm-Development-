# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.ans

    def dfs(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left_coins = self.dfs(root.left)
        right_coins = self.dfs(root.right)
        coin = left_coins + right_coins + root.val - 1
        self.ans += abs(coin)
        
        return coin
        
