# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right    
class Solution:
    def fn(self, root, ans, temp, sum, targetSum):
        if root is None:
            return
        if not root.left and not root.right and sum + root.val == targetSum:
            temp.append(root.val)
            ans.append(list(temp))
            temp.pop()
            return
        sum += root.val
        temp.append(root.val)
        self.fn(root.left, ans, temp, sum, targetSum)
        self.fn(root.right, ans, temp, sum, targetSum)
        temp.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        temp = []
        sum = 0
        self.fn(root, ans, temp, sum, targetSum)
        return ans

        
