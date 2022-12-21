class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        store=[]
        citations.reverse()
        length=len(citations)
        if(length==1):
            ran=2
        else:
            ran=length+1
        for j in range(1,ran):
            if(citations[j-1]-j>=0):
                store.append(citations[j-1]-j)
            elif(citations[0]==0):
                 return 0
        return store.index(min(store))+1
    