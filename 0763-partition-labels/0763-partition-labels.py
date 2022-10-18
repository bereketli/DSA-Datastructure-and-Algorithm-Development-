class Solution(object):
    def partitionLabels(self, s):
        l= 0
        prefi =0
        output =[]
        counted =Counter(s)
        for r  in range(len(s)):
            counted[s[r]] -=1
            while counted[s[l] ]==0 and counted[s[r]] ==0 and l < r:
                l +=1
            if l ==r  and counted[s[l] ]==0 and counted[s[r]] ==0:
                
                result = r +1 if not output else r - prefi +1
                
                output.append(result)
                prefi += output[-1]
        return output
                
            
        """
        :type s: str
        :rtype: List[int]
        """
        