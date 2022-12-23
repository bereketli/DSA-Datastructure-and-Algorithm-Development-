class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)
        for char in t:
            if char not in count_s or count_s[char] < count_t[char]:
                return char
        