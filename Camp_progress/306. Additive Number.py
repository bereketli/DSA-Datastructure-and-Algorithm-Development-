class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        self.is_additive = False
        def dfs(string, arr, i):
            if i >= len(string):
                if len(arr) > 2:
                    self.is_additive = True
                return
            
            
            num = ""
            for j in range(i, len(string)):
                num += string[j]
                if len(num) > 1 and not int(num[0]):
                    return
                if len(arr) < 2 or sum(arr[-2:]) == int(num):
                    arr.append(int(num))
                    dfs(string,[] + arr, j + 1)
                    arr.pop()
            return
        dfs(num, [], 0)
        return self.is_additive
