class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counted = Counter(nums)
        for ky in counted:
            if counted[ky] == 1:
                return ky
