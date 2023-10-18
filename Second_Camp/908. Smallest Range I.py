class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        result = (max(nums) -k )  - (min(nums) + k)
        return result if result > 0 else 0
