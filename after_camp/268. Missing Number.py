class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        set_nums = set(nums)
        for i in range(n + 1):
            if i not in set_nums:
                return i