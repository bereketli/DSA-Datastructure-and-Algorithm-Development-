class Solution(object):
    def longestBeautifulSubstring(self, word):
          count, l, maxlen=0, 0, 0
          vowel =set()
          for index, vow in enumerate(word):
                if index >0 and vow < word[index -1]:
                    vowel = set()
                    l = index 
                vowel.add(vow)
                if len(vowel) == 5 :
                    maxlen = max (maxlen, index - l +1 )
          return maxlen
                    
            
     
        