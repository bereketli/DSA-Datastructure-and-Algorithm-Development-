class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        temp = [0] * n
        return self.solve(0, n, requests, temp)
    
    def solve(self, ind, n, requests, temp):
        if ind == len(requests):
            for i in temp:
                if i != 0:
                    return float('-inf')
            return 0
        
        take, not_take = 0, 0
        u, v = requests[ind][0], requests[ind][1]
        
        temp[u] -= 1
        temp[v] += 1
        take = 1 + self.solve(ind + 1, n, requests, temp)
        temp[u] += 1
        temp[v] -= 1
        
        not_take = self.solve(ind + 1, n, requests, temp)
        
        return max(take, not_take)
        
