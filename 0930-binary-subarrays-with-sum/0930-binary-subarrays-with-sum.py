class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_store = {0:1}
        
        sum = 0
        count = 0
        for num in nums:
            sum += num
            if sum - goal in prefix_store:
                count +=  prefix_store[sum - goal] 
            if sum not in prefix_store:
                prefix_store[sum] = 1
            else:
                prefix_store[sum] +=1
          
           
        
        return count