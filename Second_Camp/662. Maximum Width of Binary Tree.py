# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        que = deque()
        que.append([root, 1])
        max_width = 0
        while que:
            left = que[0][1]
            right = que[-1][1]
            max_width = max(max_width, right - left + 1)
            tempo = deque()
            while que:
                parent = que.popleft()
                
                if parent[0].left:
                    tempo.append([parent[0].left, 2*parent[1]])
                if parent[0].right:
                    tempo.append([parent[0].right, 2*parent[1] +1])
            que = tempo
        return max_width

        

        
