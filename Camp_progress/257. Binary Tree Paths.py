# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]: 
        self.sln = []
        def path(arr, node):
            if not node:
                return
            if arr:
                new =[] + arr
                new.extend(["-",">",str(node.val)])
            else:
                new =[] + arr
                new.append(str(node.val))

            left = path(new, node.left)
            right = path(new, node.right)
            if not left and not right:
                self.sln.append("".join(new))
            
            print(arr)
            return node
        path([],root)
        return self.sln

        
