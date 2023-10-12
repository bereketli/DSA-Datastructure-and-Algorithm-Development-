class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        lps = [0] * len(needle)
        i, j = 0, 1
        while j < len(needle):
            if needle[j] == needle[i]:
                lps[j] = i + 1
                j += 1
                i += 1
                      
            elif i == 0:
                 j += 1
                
            else:
                i = lps[i - 1]
               
            
        pt_s, pt_n = 0, 0

        while pt_s < len(haystack):
            if needle[pt_n] == haystack[pt_s]:
                pt_s += 1
                pt_n += 1
            
            elif pt_n == 0:
                pt_s += 1
                
            
            else:
                pt_n = lps[pt_n -1]
            
            if pt_n == len(needle):
                return pt_s - pt_n
        return -1
            

                





    
