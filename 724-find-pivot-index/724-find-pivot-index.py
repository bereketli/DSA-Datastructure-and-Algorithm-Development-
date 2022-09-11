class Solution(object):
    def pivotIndex(self, nums):
        suma=sum(nums)
        prefix_sum=0
        for i in range(len(nums)):
            if suma-prefix_sum-nums[i]==prefix_sum:
                return i
            prefix_sum+=nums[i]
        return -1