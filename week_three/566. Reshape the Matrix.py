class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row , col= len(mat), len(mat[0])
        if row * col != r * c:
            return mat
        else:
        
            newmat =[[0] * c for i in range(r)]
            store =[ ] 
            index = 0
            for i in range(row):
                for j in range(col):
                    store.append(mat[i][j])
            print(store)
            for i in range(r):
                for j in range(c):
                    
                    newmat[i][j] = store[index]
                    index += 1
            return newmat
