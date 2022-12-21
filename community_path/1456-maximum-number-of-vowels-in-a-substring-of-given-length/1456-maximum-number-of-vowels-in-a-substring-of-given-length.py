class Solution(object):
    def maxVowels(self, s, k):
        vowel ={"a","e", "i", "o", "u"}
        count =0
        maxvowel,l =0, 0
        for r in range(len(s)):
            if r < k:
                if s[r] in vowel:
                    count +=1
                    maxvowel =count
            else:
                if s[r] in vowel:
                    count +=1
                if s[l] in vowel:
                    count -=1
                l +=1
                maxvowel = max(maxvowel, count)
                
        return maxvowel
        
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        