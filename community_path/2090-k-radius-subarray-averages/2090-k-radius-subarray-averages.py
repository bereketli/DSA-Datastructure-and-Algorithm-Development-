class Solution(object):
    def getAverages(self, nums, k):
        prefix=[nums[0]]
        output =[-1] * len(nums)
        for i in range(1,len(nums)):
            prefix.append(prefix[i - 1] + nums[i])
        for i in range(k, len(nums) - k):
            if k==i:
                output[i] =int(prefix[i +  k] / (2*k + 1))
            else:
                
                output[i] =int((prefix[i +  k] - prefix[i -k -1]) / (2*k + 1))
        return output
        """
        nums = [7,4,3,9,1,8,5,2,6], k = 3
        
        prefix =[7,11,14,23,24,32,37,39,45]
        i =4
        r =7
        l= 0
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        