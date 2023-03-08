# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.count = defaultdict(list)
        self.depth = 0
        self.max = 0
        def order(node):
            self.depth  += 1
            if not node:
                self.depth  -= 1
                return
            left = order(node.left)
            right = order(node.right)
            
            if left and right:
                self.count[self.depth].extend([left.val, right.val])
                self.max = max(self.max, self.depth)
            elif left:
                    self.count[self.depth].extend([left.val])
                    self.max = max(self.max, self.depth)
            elif right:
                    self.count[self.depth].extend([ right.val])
                    self.max = max(self.max, self.depth)
                

            self.depth  -= 1
            return node
        
        order(root)
        output = []
        if root :
            output = [[root.val]] *( self.max + 1)
            for ky in self.count:
                output[ky] = self.count.get(ky)


        return output
        