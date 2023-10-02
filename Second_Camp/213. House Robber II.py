class Solution:
    def rob(self, nums: List[int]) -> int:
        def robMoney(nums):
            prev, curr = 0, 0
            for num in nums:
                temp = curr
                curr = max(prev + num, curr)
                prev = temp
            return curr

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        return max(robMoney(nums[1:]), robMoney(nums[:-1]))

