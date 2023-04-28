# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        que = deque([[root, 0]])
        average = []
        level, count, sum  = -1, 1, 0

        while que:
            node = que.popleft()
            if node[1] != level:
                average.append(sum / count)
                sum, count, level = node[0].val, 1, node[1]
            else:
                count += 1
                sum += node[0].val

            for child in [node[0].left, node[0].right]:
                if child:
                    que.append([child, node[1] + 1])
        average.append(sum / count)
        return average[1:]
        
                

         
            

                
