class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        m = {}
        mx = 0
        for c in arr:
            if c - difference in m:
                m[c] = m[c - difference] + 1
            else:
                m[c] = 1
            mx = max(mx, m[c])
        return mx 
