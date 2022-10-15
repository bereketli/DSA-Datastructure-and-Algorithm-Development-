class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        dic ={}
        unique =set()
        occurance =0
        for i in range(len(s) - minSize +1):
            for j in range(i, i + minSize):
                unique.add(s[j])
            if len(unique) <= maxLetters:
                 
                 if s[i:i + minSize ] not in dic:
                        dic[s[i: i + minSize ]] = 1
                        occurance =max(occurance, 1)
                 else:
                    dic[s[i: i + minSize]] +=1
                    occurance = max(occurance, dic[s[i: i + minSize]])
            unique =set()
        return occurance
                    
                    
                    
                    
                        
                
        
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        