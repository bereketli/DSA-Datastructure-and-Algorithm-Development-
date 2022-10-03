class Solution(object):
    def totalSteps(self, nums):
        # [7,14,4,14,13,2,6,13]
        output =0
        stack =[]
        for i in range(len(nums)):
            tempo_len ,store=0,0
            while stack and stack[-1][0] <= nums[i]:
                      top = stack.pop()
                      tempo_len = max(tempo_len,top[1])
            if stack:
                store = tempo_len + 1
                stack.append([nums[i],store])
            else:
                
                stack.append([nums[i],0])
                
            output = max(output , store)
                
        return output
        """
        :type nums: List[int]
        :rtype: int    
        """
        