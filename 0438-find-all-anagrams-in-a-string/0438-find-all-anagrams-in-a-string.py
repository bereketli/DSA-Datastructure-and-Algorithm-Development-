class Solution(object):
    def findAnagrams(self, s, p):
        dic1 ={}
        for i in p:
            if i not in dic1:
                dic1[i] =1
            else:
                dic1[i] +=1
        l =0
        output =[]
        dic2 ={}
        lenp = len(p)
        for r in range(len(s)):
            if s[r] not in dic2:
                dic2[s[r]]  = 1
            else:
                dic2[s[r]] +=1
            if r - l +1 <lenp:
                continue
            elif r - l +1 >lenp:
                dic2[s[l]] -=1
                if dic2[s[l]] == 0:
                    del dic2[s[l]]
                l +=1
            if dic2 ==dic1:
                output.append(l)
        return output
            
             
            
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        