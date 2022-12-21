class Solution(object):
    def findRepeatedDnaSequences(self, s):
        dic = set()
        dict2 = set()
        output =[]
        for i in range(len(s)-9):
          
           
            if s[i:i+10] not in dic:
                dic.add(s[i:i + 10])
            else:
                if s[i:i+10] not in dict2:
                     output.append(s[i:i+10])
                     dict2.add(s[i:i+10])
                
    
        return output
        """
        :type s: str
        :rtype: List[str]
        """
        