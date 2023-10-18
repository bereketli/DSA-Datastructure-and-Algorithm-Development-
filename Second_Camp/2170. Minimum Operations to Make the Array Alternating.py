import heapq
class Solution:
     def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0
        elif n == 3:
            if nums[0] == nums[2]:
                return 0
            else:
                return 1

        mp1 = collections.defaultdict(int)
        mp2 = collections.defaultdict(int)

        for i in range(n):
            if i % 2 == 0:
                mp1[nums[i]] += 1
            else:
                mp2[nums[i]] += 1

        p1 = []
        p2 = []

        for key, value in mp1.items():
            heapq.heappush(p1, (-value, key))
        for key, value in mp2.items():
            heapq.heappush(p2, (-value, key))

        ans = 0

        
        if len(p1) == 1 and len(p2) == 1:
            if p1[0][1] == p2[0][1]:
                ans = n - max(-p1[0][0], -p2[0][0])
            else:
                ans = n + p1[0][0] + p2[0][0]
        elif len(p1) == 1:
            a = heapq.heappop(p1)
            b = heapq.heappop(p2)
            c = heapq.heappop(p2)
            if a[1] == b[1]:
                ans = n - max(-a[0] - c[0], -b[0])
            else:
                ans = n + a[0] + b[0]
        elif len(p2) == 1:
            a = heapq.heappop(p1)
            b = heapq.heappop(p1)
            c = heapq.heappop(p2)
            if a[1] == c[1]:
                ans = n - max(-a[0], -b[0] - c[0])
            else:
                ans = n + a[0] + c[0]
        elif p1[0][1] == p2[0][1]:
            a = heapq.heappop(p1)
            b = heapq.heappop(p1)
            c = heapq.heappop(p2)
            d = heapq.heappop(p2)
            ans = n - max(-a[0] - d[0], -b[0] - c[0])
        else:
            ans = n + p1[0][0] + p2[0][0]

        return ans


