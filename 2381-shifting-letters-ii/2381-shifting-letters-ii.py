class Solution(object):
    def shiftingLetters(self, s, shifts):
        sindex=[0] * len(s)
        for i in range(len(shifts)):
            if shifts[i][2] ==0:
                sindex[shifts[i][0]] -=1
                if shifts[i][1] < len(s) -1:
                       sindex[shifts[i][1] + 1] +=1  
            else:
                sindex[shifts[i][0]] +=1
                if shifts[i][1] < len(s) -1:
                       sindex[shifts[i][1] + 1] -=1  
                
        print(sindex)
        output=[]
        prefix =0
        alphabet ="abcdefghijklmnopqrstuvwxyz"
        for i in range(len(s)):
            prefix +=sindex[i]
           
            output.append(alphabet[(-97 +ord(s[i]) + prefix) % 26])
        return "".join(output)
        
        """
        sindex ="-111-21-100"
        s = "abcdigtou", shifts = [[0,3,0],[1,2,1],[2,4,1]]
             "zbdhgs"
        
        
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        