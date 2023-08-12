class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque()
        maxDist = m + n
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = maxDist
        
        while queue:
            row, col = queue.popleft()
            for d_row, d_col in dirs:
                new_row, new_col = row + d_row, col + d_col
                if 0 <= new_row < m and 0 <= new_col < n and mat[new_row][new_col] > mat[row][col] + 1:
                    mat[new_row][new_col] = mat[row][col] + 1
                    queue.append((new_row, new_col))
        
        return mat
