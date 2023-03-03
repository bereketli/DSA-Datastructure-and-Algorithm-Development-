class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_arr = []
        sum = 0
        for num in nums:
            sum += num
            prefix_arr.append(sum)
        return prefix_arr