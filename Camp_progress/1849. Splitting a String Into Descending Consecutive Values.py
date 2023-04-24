class Solution:
    def splitString(self, s: str) -> bool:
        self.issplitable = False
        def split(s, arr, i):
            if i >= len(s):
                if len(arr) >1 and arr[-2] - arr[-1] == 1:
                    self.issplitable = True
                return
            num = ""
            for j in range(i, len(s)):
                num += s[j]
                if not arr or arr[-1] - 1 == int(num):
                    arr.append(int(num))
                    split(s, [] +arr,  j + 1)
                    arr.pop()

                elif arr and arr[-1] - 1 < int(num):
                    return
              
            return
                
        split(s,[], 0)
        return self.issplitable
