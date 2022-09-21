class Solution(object):
    def subarraySum(self, nums, k):
        prefix_store ={0:1}
        prefix_sum =0
        count =0
        for num in nums:
          
            prefix_sum += num;
            if prefix_sum -k in prefix_store:
                count+=prefix_store[prefix_sum-k]
            if prefix_sum not in prefix_store:
                prefix_store[prefix_sum] =1
            else:
                prefix_store[prefix_sum] +=1
           
           
        
        return count 
                
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        