class Solution(object):
    def topKFrequent(self, nums, k):
        count_dict = Counter(nums)
        output = []
        for num in count_dict.most_common(k):
          output.append(num[0])
        return output
        
                
            
        """
     
        
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        