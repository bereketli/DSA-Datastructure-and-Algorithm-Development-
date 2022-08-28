class Solution(object):
    def findOriginalArray(self, changed):
         store=[]
         changed.sort()
       
            
         i=0
         j=1
         while i<len(changed):
            if j<=i:
                j=i+1
            
            if changed[i]=="l":
                i+=1
                continue
            while j<len(changed) and changed[i]*2!=changed[j]:
                j+=1
          
            if j==len(changed):
                return []
            store.append(changed[i])
            changed[j]="l"
            i+=1
         return store 
                
        
                
     
        