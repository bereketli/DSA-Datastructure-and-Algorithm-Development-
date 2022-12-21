class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        count,l,prefi =0,0,1
        for i in range(len(nums)):
            prefi *= nums[i]
            while l <= i and  prefi >= k:
                prefi /= nums[l]
                l +=1
            count += i -l +1
        return count
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        