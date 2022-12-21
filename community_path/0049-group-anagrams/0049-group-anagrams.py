class Solution(object):
    def groupAnagrams(self, strs):
        order = {}
        output=[] 
        for i in range(len(strs)):
          
            arranged="".join(sorted(strs[i]))
           
            if arranged not in order:
                order[arranged] =[strs[i]]
            else:
              
                order[arranged].append(strs[i])
        for key, value in order.items():
            output.append(value)
        return output
    
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        