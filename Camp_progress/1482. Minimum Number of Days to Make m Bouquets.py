class Solution:
      def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def calc(a, days, m, k):
            no = 0
            c = 0
            for i in range(len(a)):
                if a[i] <= days:
                    c += 1
                else:
                    no += c // k
                    c = 0
            no += c // k
            return no >= m

        max_bloom = max(bloomDay)
        min_bloom = min(bloomDay)
        ans = -1

        while min_bloom <= max_bloom:
            mid = min_bloom + (max_bloom - min_bloom) // 2
            can = calc(bloomDay, mid, m, k)
            
            if can:
                ans = mid
                max_bloom = mid - 1
            else:
                min_bloom = mid + 1

        return ans

