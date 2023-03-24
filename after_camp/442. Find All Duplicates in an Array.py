class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        duplicate = []
        while i < len(nums):
            if i + 1 != nums[i] and nums[nums[i] - 1 ]!= nums[i]:
                next_position = nums[i] - 1
                nums[i], nums[next_position] = nums[next_position], nums[i]

            else:
                i += 1
        for i, val in enumerate(nums):
            if i + 1 != nums[i]:
                duplicate.append(nums[i])
        return duplicate
        