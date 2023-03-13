class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        sindex=[0] * len(s)
        for i in range(len(shifts)):
            if shifts[i][2] == 0:
                sindex[shifts[i][0]] -= 1
                if shifts[i][1] < len(s) -1:
                       sindex[shifts[i][1] + 1] += 1  
            else:
                sindex[shifts[i][0]] += 1
                if shifts[i][1] < len(s) -1:
                       sindex[shifts[i][1] + 1] -= 1  
                
       
        output=[]
        prefix =0
        
        for i in range(len(s)):
            prefix +=sindex[i]
           
            output.append(chr(97+(-97 +ord(s[i]) + prefix) % 26))
        return "".join(output)
        
        """
        sindex ="-111-21-100"
        s = "abcdigtou", shifts = [[0,3,0],[1,2,1],[2,4,1]]
             "zbdhgs"
        
        
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """