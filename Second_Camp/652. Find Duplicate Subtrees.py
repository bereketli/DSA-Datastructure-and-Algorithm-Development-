# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.output = []
        self.subtree_count = defaultdict(int)
        
        def dfs(node):
            if not node:
                return "null"
            
           
            serial = str(node.val) + "," + dfs(node.left) + "," + dfs(node.right)
            
            self.subtree_count[serial] += 1
            if self.subtree_count[serial] == 2:
                self.output.append(node)
            
            return serial

        dfs(root)
        return self.output
