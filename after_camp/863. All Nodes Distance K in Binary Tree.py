# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        #build undirected grpah
        def build(node):
            if not node:
                return 
            
            left = build(node.left)
            right = build(node.right)
           
            if right  and left:
                graph[node.val].append(left.val)
                graph[node.val].append(right.val)
                graph[right.val].append(node.val)
                graph[left.val].append(node.val)
            elif right:
                graph[node.val].append(right.val)
                graph[right.val].append(node.val)
            elif left:
                graph[node.val].append(left.val)
                graph[left.val].append(node.val)
            return node
        build(root)
        output = []
        visited = set()
        def dfs(node, depth, graph, visited):
           
            visited.add(node)
            if depth > k:
                return
            elif depth == k:
                output.append(node)
                return
            
            for child in graph[node]:
                if child not in visited:
                    dfs(child, depth + 1, graph, visited)
            return  

        dfs(target.val, 0, graph, visited)
        return output


            




        
