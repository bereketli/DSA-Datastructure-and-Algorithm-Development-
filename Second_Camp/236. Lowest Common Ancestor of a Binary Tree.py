class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': 
        candidate = set([p.val, q.val]) 
        self.common = 0

        def dfs(node):
            if not node:
                return 0
              
            left = dfs(node.left)
            right = dfs(node.right)
            count = 0
            if node.val in candidate:
                count += 1
            output = left + right + count
            if output == 2:

                self.common = node
                return 0
            return output
        dfs(root)
        return self.common


       
