class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=[]
        dictst = {}
        for i in range(n):
            
            arr.append(i+1)
        j=-1

        while len(arr)>1:
            index=((j+k)%len(arr))
   
            arr.pop(index)

            j=index-1
        return arr[-1]
