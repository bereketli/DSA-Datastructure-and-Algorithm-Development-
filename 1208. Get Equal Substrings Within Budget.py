class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        prefi_diff=[]
        prefi =0
        for i in range(len(s)):
            prefi += abs(ord(s[i]) - ord(t[i]))
            prefi_diff.append(prefi)
        l, maxilen =0,0
        for r in range(len(prefi_diff)):
            left =prefi_diff[l - 1] if l >0 else 0
            while prefi_diff[r] - left > maxCost:
                l +=1
                left =prefi_diff[l - 1]
            maxilen= max(maxilen, r - l +1)
        return maxilen
            
            
        """
        differ=[1,2,3,6]
        s = "abcd", t = "bcdf", maxCost = 3
        l =0
        r =1
        prefi = 1
        ans=1
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """