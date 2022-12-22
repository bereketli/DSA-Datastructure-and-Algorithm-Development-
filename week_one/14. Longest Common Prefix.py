class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = len(strs[0])
        for strin in strs:
            i=0
            while (i < first and i < len(strin)) and strs[0][i] == strin[i]  :
                i +=1
            first =i
        return strs[0][:first]
                                                                                                                                                                                                                                                                                                                                                                                                                   
