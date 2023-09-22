class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [0] * (n + 1)

        for val in nums:
            if 1 <= val <= n:  
                ans[val] = 1

        for i in range(1, len(ans)):
            if ans[i] == 0:
                return i

        return len(ans)
        
