class Solution(object):
    def subarraysDivByK(self, nums, k):
        remaind ={0:1}
        prefi , count = 0, 0
        for num in nums:
            prefi += num
            if prefi % k in remaind:
                count += remaind[prefi % k]
                remaind[prefi % k] +=1
            else:
                remaind[prefi % k] = 1
        return count
            
        """
         a, b and if 0 = (b- a) % k
         remainder ={0:2 , 4:4, 2:1}
         prefi =5
         ans = 7
         is prefi % k in remainder:
         ans +=1
        

        :type nums: List[int]
        :type k: int
        :rtype: int
        """