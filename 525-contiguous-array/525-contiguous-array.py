class Solution(object):
    def findMaxLength(self, nums):
        summed ={0:-1}
        max_len, count =0,0
        for i, num in enumerate(nums):
            if num == 0:
                count -=1
            else:
                count +=1
            if count in summed:
                max_len = max( max_len, i - summed[count])
            else:
                summed[count] = i
        return max_len
        
        
        
        
        """
        :type nums: List[int]
        :rtype: int
         """
        