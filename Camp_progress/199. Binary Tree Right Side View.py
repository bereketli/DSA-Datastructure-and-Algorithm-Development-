# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            que = deque([root])
            right_view = [root.val]
            while que:
            
                tempo = deque()
                while que:
                    parent = que.popleft()
                    if parent.left: tempo.append(parent.left)
                    if parent.right: tempo.append(parent.right) 
               
                que = tempo
                if que:
                    right_view.append(que[-1].val)
            
            return right_view
        
        
            

            
        
