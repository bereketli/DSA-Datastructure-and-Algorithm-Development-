class Solution(object):
    def sortSentence(self, s):
        senten=s.split()
        for i in range(1,len(senten)):
            j=i-1
            store=senten[i]
            while j>=0 and store[-1]<senten[j][-1]:
                senten[j+1]=senten[j]
                j-=1
                
            senten[j+1]=store
            i+=1
            
        
        for i in range(len(senten)):
             senten[i]=senten[i][:-1]
        output=" ".join(senten)
        return output
       
        """
        :type s: str
        :rtype: str
        """
        