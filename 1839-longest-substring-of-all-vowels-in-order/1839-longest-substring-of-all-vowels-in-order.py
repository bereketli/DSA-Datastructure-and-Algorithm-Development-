class Solution(object):
    def longestBeautifulSubstring(self, word):
        vowel ={"a":1, "e":2 , "i":3, "o":4 , "u":5}
        count, maxlen =1,0
        l, r =0,0
        while r < len(word):
          
            if l==0 and word[r] == "a" and word[l] !="a":
              
                   l = r
            elif l == 0 and word[l] != "a":
                r +=1
                continue
            if vowel[word[r-1]] == vowel[word[r]] - 1:
                    count +=1
            elif (vowel[word[r-1]] != vowel[word[r]] - 1  and word[r-1] != word[r]) :
                if count ==  5:
                       maxlen = max(maxlen, r - l )
                l = r
                while l<len(word) and word[l] != "a":
                    l +=1
                r = l + 1
                if r<len(word)-1:
                    count = 1
                continue
            r += 1
        
        if count ==  5:
                       maxlen = max(maxlen, r - l )
        return maxlen
                    
            
                    
        """
        :type word: str
        :rtype: int
        """
        