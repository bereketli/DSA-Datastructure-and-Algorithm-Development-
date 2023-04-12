"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.depth = 0
        def max_depth(node, depth):
            if not node:
                return
            depth += 1
            self.depth = max(self.depth, depth)
            for i in range(len(node.children)):
                max_depth(node.children[i], depth)
            return

        max_depth(root, 0)
        return self.depth
        
                
