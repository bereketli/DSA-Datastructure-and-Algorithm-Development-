class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        parent = [i for i in range(n)]

        def areSimilar(X, Y):
            if X == Y:
                return True
            count = 0
            for i in range(len(X)):
                if X[i] != Y[i]:
                    count += 1
                    if count > 2:
                        return False
            return count == 2

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        for i in range(n):
            for j in range(i + 1, n):
                if areSimilar(strs[i], strs[j]):
                    parentI = find(i)
                    parentJ = find(j)
                    if parentI != parentJ:
                        parent[parentI] = parentJ

        count = 0
        for i in range(n):
            if parent[i] == i:
                count += 1

        return count

        
