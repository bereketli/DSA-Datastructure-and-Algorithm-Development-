class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count ={}
        longest, l =0, 0
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] =1
            else:
                count[s[r]] +=1
            while count[s[r]] >1:
                count[s[l]] -=1
                l+=1
            longest = max(longest, r - l +1)
        return longest
                
        
       
       
        """
        s = "abcabcbb"
        count ={a:2,b:2, c:1 }
        l =2
        r =2
        regis =3
        :type s: str
        :rtype: int
        """
        

