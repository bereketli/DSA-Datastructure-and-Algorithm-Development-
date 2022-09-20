class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l,maxlen =0,0
        no_char={}
        for r ,char in enumerate(s):
            if char not in  no_char:
                no_char[char] =1
            else:
                no_char[char] +=1
            while no_char[char] >1:
               no_char[s[l]] -=1
               l +=1
            maxlen =max(maxlen, r -l +1)
        return maxlen
        """
        :type s: str
        :rtype: int
        """
        