class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
             if num not in dic:
                dic[num] = 0
        for num in nums:
            num = list(str(num))
            num.reverse()
            num ="".join(num)
            num = int(num)
            
            if num not in dic:
                dic[num] = 0
        
        return len(dic)

