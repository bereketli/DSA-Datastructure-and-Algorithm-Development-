# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def finder(node):
            curr = node
            while curr.left:
                curr = curr.left
            return curr.val
        def deletSucessor(node):
            curr = node
            while  curr.left and curr.left.left:
                curr = curr.left
            return curr
        def delet(node, key):
            if not node :
                return node
            elif key > node.val:
                node.right = delet(node.right, key)
            elif key < node.val:
                node.left = delet(node.left, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    
                    node.val = finder(node.right)
                    key = node.val
                    node.right= delet(node.right, key)
            return node
        
        return delet(root, key)
                    
                    
        