class Solution(object):
    def subarraySum(self, nums, k):
        prefix_sum = {0:1}
        count,summed = 0,0
        for num in nums:
            summed += num
            if summed - k in prefix_sum:
                count += prefix_sum[summed - k]
            if summed not in prefix_sum:
                prefix_sum[summed] = 1
            else:
                prefix_sum[summed] += 1
        return count
        
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        