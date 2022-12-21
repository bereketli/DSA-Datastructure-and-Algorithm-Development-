class Solution(object):
    def findTheWinner(self, n, k):
        arr=[]
        for i in range(n):
            arr.append(i+1)
            j=-1

        while len(arr)>1:
            index=((j+k)%len(arr))
   
            arr.pop(index)

            j=index-1
        return arr[-1]