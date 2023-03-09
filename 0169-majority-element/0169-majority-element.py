class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counted = Counter(nums)
        for ky in counted:
            if counted[ky] > len(nums)/2:
                return ky