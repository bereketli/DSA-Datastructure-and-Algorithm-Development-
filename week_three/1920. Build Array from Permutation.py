class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        permutate = []
        for index in nums:
            permutate.append(nums[index])
        return permutate