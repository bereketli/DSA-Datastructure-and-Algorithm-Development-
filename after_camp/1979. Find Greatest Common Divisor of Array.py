class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        num = gcd(largest, smallest)
        return num
