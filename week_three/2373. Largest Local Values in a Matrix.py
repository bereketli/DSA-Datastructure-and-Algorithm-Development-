class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        queue = deque()
        output = [[0] *(n -2) for _ in range(n - 2)]
        tempo = [[0] * (n - 2) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                queue.append(grid[i][j])
                if len(queue) == 3:
                    tempo[i][j-2] = max(queue)
                    queue.popleft()
            queue.clear()
        queue = deque()
        for i in range(len(tempo[0])):
            for j in range(len(tempo)):
                queue.append(tempo[j][i])
                if len(queue) == 3:
                    output[j - 2][i] = max(queue)
                    queue.popleft()
            queue.clear()
        return output

        
       
