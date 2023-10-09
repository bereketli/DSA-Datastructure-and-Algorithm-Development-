class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        memo = [[-1] * n for _ in range(m)]

        def backTrack(i, j):
            if i == m or j == n:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]

            memo[i][j] = max(
                1 + backTrack(i + 1, j + 1) if nums1[i] == nums2[j] else 0,
                backTrack(i, j + 1),
                backTrack(i + 1, j)
            )

            return memo[i][j]

        return backTrack(0, 0)

    
        
