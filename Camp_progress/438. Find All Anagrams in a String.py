class Solution(object):
    def findAnagrams(self, s, p):
        dic1 ={}
        output =[]
        for i in range(len(p)):
            if p[i] not in dic1:
                dic1[p[i]] =1
            else:
                dic1[p[i]] +=1
        dic2 ={}
        l =0
        for r in range(len(s)):
             if s[r] not in dic2:
                    dic2[s[r]] =1
             else:
                    dic2[s[r]] +=1
             
             if r >len(p) -1:
                if dic2[s[l]] == 1:
                    del dic2[s[l]]
                else:
                    dic2[s[l]] -=1
                l +=1
            
             if dic1 == dic2:
                output.append(l)
        return output
                    
                
       
            
             
            
        """
        s = "cbaebabacd", p = "abc"
        dic1 ={
        a:1
        b:1
        c:1
        }
        l =1
        r =2
        dic2{
        
        b:1
        a:1
        e:1
        }
        
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        

